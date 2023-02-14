from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
from polyQ.models import Disease
from django.db.models import Q
from django.contrib import messages
from django.core.management import CommandError
from django.template import RequestContext
from django.utils import translation
from .models import Introduction
# from translations.models import Translation ---- Using the django-translations package
from django.db.models import Prefetch


# Internalization 
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext




# Views and render templates

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home/index.html')


def objectives(request):
    return render(request, 'objectives/index.html')


# def diseases_drpla(request):
#     return render(request, 'diseases/drpla/index.html')
#
#
# def diseases_hd(request):
#     return render(request, 'diseases/hd/index.html')
#
#
# def diseases_sbma(request):
#     return render(request, 'diseases/sbma/index.html')
#
#
# def diseases_sca1(request):
#     return render(request, 'diseases/sca1/index.html')
#
#
# def diseases_sca2(request):
#     return render(request, 'diseases/sca2/index.html')
#
#
# def diseases_sca3(request):
#     return render(request, 'diseases/sca3/index.html')
#
#
# def diseases_sca6(request):
#     return render(request, 'diseases/sca6/index.html')
#
#
# def diseases_sca7(request):
#     return render(request, 'diseases/sca7/index.html')
#
#
# def diseases_sca17(request):
#     return render(request, 'diseases/sca17/index.html')


def contact(request):
    return render(request, 'contact/index.html')


def authors(request):
    return render(request, 'authors/index.html')


def appreciation(request):
    return render(request, 'appreciation/index.html')


# def disease_view(request, disease_name):
#     test_list = [1, 2, 3, 4, 5]
#     try:
#         disease = Disease.objects.get(name=disease_name)
#         return render(request, 'test.html', {'disease': disease, 'test_list': test_list})
#     except Disease.DoesNotExist:
#         error_message = "This disease does not exit on our database"
#         return render(request, 'not-found-page.html', {'error_message': error_message})


def tmp_disease(request):
    return render(request, 'test.html')


def search_disease(request):
    style_1_diseases = ["HD", "DRPLA", "SBMA", "SCA6"]
    style_2_diseases = ["SCA1", "SCA2", "SCA3", "SCA7", "SCA17"]
    disease_name = request.GET.get(_('disease'))
    try:
        disease_name = request.GET.get(_('disease'))
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
            'style_1_diseases': style_1_diseases,
            'style_2_diseases': style_2_diseases,
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


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)


