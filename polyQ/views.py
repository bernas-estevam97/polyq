import logging
import string
from datetime import date
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode, urlparse, parse_qs

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from feedback.forms import FeedbackForm
from polyQ.models import Disease

logger = logging.getLogger(__name__)

# Everything the disease page template touches, loaded in a fixed number of queries
# instead of one query per reference, link, list and image.
DISEASE_SELECT = ('introduction', 'first_described', 'epidemiology', 'causative_gene',
                  'codified_protein', 'patho_physiology', 'clinical', 'characteristic_table',
                  'css_class', 'added_info')
DISEASE_PREFETCH = ('epidemiology__image', 'causative_gene__image', 'codified_protein__image',
                    'patho_physiology__image', 'characteristic_table__rows_col', 'list__item',
                    'references__links', 'trials', 'coordinates')

def normalize_text(text):
    text = unicodedata.normalize('NFKD', text)
    return text.replace("’", "'").strip()

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home/index.html')


def objectives(request):
    return render(request, 'objectives/index.html')


def contact(request):
    return render(request, 'contact/index.html')


def authors(request):
    return render(request, 'authors/index.html')


def appreciation(request):
    return render(request, 'appreciation/index.html')


def support(request):
    return render(request, 'support/index.html')

# Create a thread pool executor for the application
executor = ThreadPoolExecutor(max_workers=3)

# Function to send email notifications in the background.
# Runs in a worker thread, so exceptions would otherwise vanish silently: log them.
def send_notification_emails(form_data, email_address, page=''):
    try:
        _send_notification_emails(form_data, email_address, page)
    except Exception:
        logger.exception("Feedback notification email failed")


def _send_notification_emails(form_data, email_address, page=''):
    # Sender and admin recipient come from .env (FEEDBACK_FROM_EMAIL / FEEDBACK_ADMIN_EMAIL)
    email_from = settings.DEFAULT_FROM_EMAIL
    context = {
        'name': string.capwords(form_data['visitor_name']),
        'email': email_address,
        'subject': form_data['subject'],
        'message': form_data['message'],
        'page': page or '(unknown)',
        'site_url': settings.SITE_URL,
        'admin_url': settings.SITE_URL + reverse('admin:feedback_form_changelist'),
        'year': date.today().year,
    }

    # Admin notification: the whole message, and Reply-To set to the visitor so a plain
    # "Reply" in the inbox answers them directly.
    if settings.FEEDBACK_ADMIN_EMAIL:
        EmailMessage(
            subject=f"PolyQ feedback: {context['subject']}",
            body=render_to_string('emails/feedback_admin.txt', context),
            from_email=email_from,
            to=[settings.FEEDBACK_ADMIN_EMAIL],
            reply_to=[email_address] if email_address else None,
        ).send()
    else:
        logger.warning("FEEDBACK_ADMIN_EMAIL is not set in .env: admin was not notified of new feedback")

    # Email is optional on the form: no address, no confirmation email
    if not email_address:
        return

    # Confirmation to the visitor: HTML with a plain-text version (better for spam filters
    # and text-only mail clients)
    confirmation = EmailMultiAlternatives(
        subject="We received your message - PolyQ Database",
        body=render_to_string('emails/feedback_confirmation.txt', context),
        from_email=email_from,
        to=[email_address],
    )
    confirmation.attach_alternative(render_to_string('emails/feedback_confirmation.html', context), 'text/html')
    confirmation.send()

def redirect_with_query_param(request, new_params: dict):
    """
    Redirects to the same path with updated query parameters.
    Preserves the 'disease' parameter and adds/updates others.
    """
    url_parts = urlparse(request.get_full_path())
    query_dict = parse_qs(url_parts.query)
    # Drop the previous outcome, or a failed attempt followed by a successful one
    # would leave both ?error and ?sent in the URL and the error popup would win.
    query_dict.pop('sent', None)
    query_dict.pop('error', None)

    # Always retain the disease query parameter if it's available
    disease_name = request.GET.get('disease', '')
    if disease_name:
        query_dict['disease'] = [disease_name]


    # Add or modify other parameters as needed
    for key, value in new_params.items():
        query_dict[key] = [value]

    # Rebuild the query string
    new_query = urlencode(query_dict, doseq=True)
    return HttpResponseRedirect(f"{url_parts.path}?{new_query}")


# Main view function with rate-limiting and email sending in background
def search_disease(request):
    # request.GET is already URL-decoded; decoding again would turn a literal "+" into a space
    disease_name = normalize_text(request.GET.get('disease', ''))
    # request.csp_nonce is lazy and is falsy until read as a string, so the reCAPTCHA widget
    # would skip it. str() generates it now; the NONCE entry in settings puts it in the header.
    nonce = str(request.csp_nonce)
    form = FeedbackForm(request.POST or None, nonce=nonce)
    message_error = 'Something went wrong, try again!'
    message_success = "Form sent. Thanks for contacting us!"

    # ✅ Read redirect status from query params (for GET requests after redirect)
    sent_flag = request.GET.get('sent')
    error_flag = request.GET.get('error')

    sent = sent_flag in ['True', 'mailTrue']
    error = error_flag is not None

    if request.method == 'POST':
        if form.is_valid():
            if form.is_spam():
                return redirect_with_query_param(request, {'sent': 'True'})

            form.save()

            # Send email notifications in the background
            email_address = form.cleaned_data.get('email')
            recipient = email_address if email_address else ""
            # page: which disease page the form was sent from, shown in the admin email
            executor.submit(send_notification_emails, form.cleaned_data, recipient, disease_name)

            # Reset the form after submission
            return redirect_with_query_param(request, {'sent': 'mailTrue'})

        else:
            return redirect_with_query_param(request, {'error': 'true'})

    # Gather data for the disease search: exact name, then exact slug, then a loose match
    query = disease_name.strip()
    disease = None
    if query:
        disease = (Disease.objects.filter(name__iexact=query).first()
                   or Disease.objects.filter(slug__iexact=query).first()
                   or Disease.objects.filter(Q(name__icontains=query) | Q(slug__icontains=query))
                   .order_by('id').first())  # several loose matches (e.g. "ataxia"): pick consistently

    if disease is None:
        return render(request, 'not-found-page.html',
                      {'error_message': "This disease does not exist in our database."}, status=404)

    disease = (Disease.objects.select_related(*DISEASE_SELECT)
               .prefetch_related(*DISEASE_PREFETCH).get(pk=disease.pk))

    other_diseases = Disease.objects.exclude(id=disease.id)
    img_coordinates = [
        {
            'x': coord.x,
            'y': coord.y,
            'title': coord.title,
            'text': coord.text,
            'resolution': coord.resolution
        }
        for coord in disease.coordinates.all()
    ]

    context = {
        'disease': disease,
        'title': disease.name,
        'other_diseases': other_diseases,
        'img_coordinates': img_coordinates,
        'form': form,
        'message_error': message_error,
        'message_success': message_success,
        'sent': sent,
        'error': error
    }

    return render(request, 'diseases.html', context)


def custom_page_not_found_view(request, exception):
    error_code = "404"
    error_message = "Page not found"
    # Without an explicit status these pages were served as 200 OK ("soft 404"),
    # so search engines indexed them and monitoring saw no errors.
    return render(request, "not-found-page.html", {'error_message': error_message, 'error_code': error_code},
                  status=404)


def custom_error_view(request, exception=None):
    error_code = "500"
    error_message = "Internal Server error"
    return render(request, "not-found-page.html", {'error_message': error_message, 'error_code': error_code},
                  status=500)


