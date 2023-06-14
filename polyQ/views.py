from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
from polyQ.models import Disease
from django.db.models import Q
from django.contrib import messages
from django.core.management import CommandError
from django.template import RequestContext


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
    disease_name = request.GET.get('disease')
    try:
        disease_name = request.GET.get('disease')
        disease = Disease.objects.get(
            Q(name=disease_name.upper()) | Q(slug__contains=disease_name))
        other_diseases = Disease.objects.all().exclude(name=disease_name.upper())
        title = disease.name
        img_coordinates = []

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
            'img_coordinates': img_coordinates
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
