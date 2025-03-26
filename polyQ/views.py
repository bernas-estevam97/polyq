from django.http import HttpResponse, HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
from polyQ.models import Disease
from django.db.models import Q
from django.contrib import messages
from django.core.management import CommandError
from django.template import RequestContext
from feedback.forms import FeedbackForm
from django.core import mail
from django.core.mail import EmailMessage, send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
import string
import html
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode, urlparse, parse_qs


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

# Create a thread pool executor for the application
executor = ThreadPoolExecutor(max_workers=3)

# Function to send email notifications in the background
def send_notification_emails(form_data, email_address):
    # Send email to admin
    send_mail(
        f"Form received notification from PolyQ",
        f"You received a feedback form from visitor: {string.capwords(form_data['visitor_name'])}\n"
        f"Be sure to check it when you are available\n\n"
        f"PolyQ Database automated form notification",
        "polyqdatabase@gmail.com",
        ["bernaz10.1997golden@gmail.com"],
        fail_silently=False,
    )

    # Send email to the user
    subject = f"Your form was submitted to PolyQDatabase, {string.capwords(form_data['visitor_name'])}."
    subject_form = form_data['subject']
    email_from = settings.EMAIL_HOST_USER
    email_to = [email_address]
    message = form_data['message']
    mydict = {'subject': subject_form, 'name': form_data['visitor_name'], 'message': message}
    html_message = render_to_string('mail_template.html', context=mydict)
    email_for_visitor = EmailMessage(subject, html_message, email_from, email_to)
    email_for_visitor.content_subtype = 'html'
    email_for_visitor.send()

def redirect_with_query_param(request, new_params: dict):
    """
    Redirects to the same path with updated query parameters.
    Preserves the 'disease' parameter and adds/updates others.
    """
    url_parts = urlparse(request.get_full_path())
    query_dict = parse_qs(url_parts.query)

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
    disease_name = request.GET.get('disease')
    form = FeedbackForm(request.POST or None)
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
            executor.submit(send_notification_emails, form.cleaned_data, recipient)

            # Reset the form after submission
            return redirect_with_query_param(request, {'sent': 'mailTrue'})

        else:
            return redirect_with_query_param(request, {'error': 'true'})

    # Gather data for the disease search
    try:
        disease = Disease.objects.get(Q(name=disease_name.upper()) | Q(slug__contains=disease_name))
        other_diseases = Disease.objects.exclude(name=disease_name.upper())
        title = disease.name
        img_coordinates = [
            {
                'x': coord.x,
                'y': coord.y,
                'title': coord.title,
                'text': coord.text,
                'device': coord.device
            }
            for coord in disease.coordinates.all()
        ]

        context = {
            'disease': disease,
            'title': title,
            'other_diseases': other_diseases,
            'img_coordinates': img_coordinates,
            'form': form,
            'message_error': message_error,
            'message_success': message_success,
            'sent': sent,
            'error': error
        }

        return render(request, 'diseases.html', context)

    except Disease.DoesNotExist:
        return render(request, 'not-found-page.html', {'error_message': "This disease does not exist in our database!"})
    except Disease.MultipleObjectsReturned:
        return render(request, 'home/index.html', {'error_message': "Be more specific with your search."})



def custom_page_not_found_view(request, exception):
    error_code = "404"
    error_message = "Page not found"
    return render(request, "not-found-page.html", {'error_message': error_message, 'error_code': error_code})


def custom_error_view(request, exception=None):
    error_code = "500"
    error_message = "Internal Server error"
    return render(request, "not-found-page.html", {'error_message': error_message, 'error_code': error_code})


