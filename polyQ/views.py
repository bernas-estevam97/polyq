from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
from polyQ.models import Disease
from django.db.models import Q
from django.contrib import messages
from django.core.management import CommandError
from django.template import RequestContext
from feedback.forms import FeedbackForm
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags



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


def search_disease(request):
    form = FeedbackForm
    disease_name = request.GET.get('disease')
    message_error = 'Something went wrong, try again!'
    message_success = "Form sent. Thanks for contacting us!"
    sent = False
    error=False
    try:
        disease_name = request.GET.get('disease')
        disease = Disease.objects.get(
            Q(name=disease_name.upper()) | Q(slug__contains=disease_name))
        other_diseases = Disease.objects.all().exclude(name=disease_name.upper())
        title = disease.name
        img_coordinates = []
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid() and not form.data['email']:
                form.save()
                form = FeedbackForm()
                sent = True
                return HttpResponseRedirect('/disease_search/?disease='+ disease_name + '&sent=True')
            elif form.is_valid() and form.data['email']:
                form.save()
                # send_mail(
                #             f"Thank you for your feedback, Mr/Mrs.{form.data['visitor_name']}",
                #             f"Here are the details you inputed into our form.\n"
                #             f"Subject: {form.data['subject']}\n" 
                #             f"Message: {form.data['message']}\n\n"
                #             f"Thank you again for contacting us.\n" 
                #             f"Best regards\nPolyQDatabase team",
                #             "polyqdatabase@gmail.com",
                #             [form.data['email']],
                #             fail_silently=False,
                #         )
                subject = f"Your form was submitted to PolyQDatabase, Mr/Mrs. {form.data['visitor_name']}."
                subject_form = form.data['subject']
                
                email_from = settings.EMAIL_HOST_USER
                email_to = [form.data['email']]
                message = form.data['message']
                mydict= {'subject': subject_form, 'name': form.data['visitor_name'], 'message': message}
                html_message = render_to_string('mail_template.html', context=mydict)
                # plain_message = strip_tags(html_message)
                email = EmailMessage(subject, html_message, email_from, email_to)
                email.content_subtype = 'html'
                email.send()
                form = FeedbackForm()
                sent = True
                return HttpResponseRedirect('/disease_search/?disease='+ disease_name + '&sent=mailTrue')
            else:
                error=True
                return HttpResponseRedirect('/disease_search/?disease='+ disease_name + '&error')
        else:
            form = FeedbackForm
            if 'sent' in request.GET:
                sent = True
            if 'error' in request.GET:
                error=True

        for img_coordinate in disease.coordinates.all():
            img_object = {
                'x': img_coordinate.x,
                'y': img_coordinate.y,
                'title': img_coordinate.title,
                'text': img_coordinate.text,
                'device': img_coordinate.device
            }
            img_coordinates.append(img_object)
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
        error_code = ""
        error_message = "This disease does not exit on our database!"
        return render(request, 'not-found-page.html', {'error_message': error_message, 'error_code': error_code})

    except Disease.MultipleObjectsReturned:
        error_code = ""
        error_message = "Be more specific with your search"
        return render(request, 'home/index.html', {'error_message': error_message, 'error_code': error_code})
        # raise CommandError(error_message_alert)


def custom_page_not_found_view(request, exception):
    error_code = "404"
    error_message = "Page not found"
    return render(request, "not-found-page.html", {'error_message': error_message, 'error_code': error_code})


def custom_error_view(request, exception=None):
    error_code = "500"
    error_message = "Internal Server error"
    return render(request, "not-found-page.html", {'error_message': error_message, 'error_code': error_code})


