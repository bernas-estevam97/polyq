from django.http import HttpResponse
from django.shortcuts import render

from polyQ.models import Disease
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home/index.html')


def objectives(request):
    return render(request, 'objectives/index.html')


def diseases_drpla(request):
    return render(request, 'diseases/drpla/index.html')


def diseases_hd(request):
    return render(request, 'diseases/hd/index.html')


def diseases_sbma(request):
    return render(request, 'diseases/sbma/index.html')


def diseases_sca1(request):
    return render(request, 'diseases/sca1/index.html')


def diseases_sca2(request):
    return render(request, 'diseases/sca2/index.html')


def diseases_sca3(request):
    return render(request, 'diseases/sca3/index.html')


def diseases_sca6(request):
    return render(request, 'diseases/sca6/index.html')


def diseases_sca7(request):
    return render(request, 'diseases/sca7/index.html')


def diseases_sca17(request):
    return render(request, 'diseases/sca17/index.html')


def contact(request):
    return render(request, 'contact/index.html')


def authors(request):
    return render(request, 'authors/index.html')


def appreciation(request):
    return render(request, 'appreciation/index.html')


def disease_view(request, disease_name):
    test_list = [1, 2, 3, 4, 5]
    try:
        disease = Disease.objects.get(name=disease_name)
        return render(request, 'test.html', {'disease': disease, 'test_list': test_list})
    except Disease.DoesNotExist:
        error_message = "This disease does not exit on our database"
        return render(request, 'not-found-page.html', {'error_message': error_message})



def tmp_disease(request):
    return render(request, 'test.html')

def search_disease(request):
    disease_name = request.GET.get('disease')
    try:
        disease = Disease.objects.get(Q(name__contains=disease_name) | Q(slug__contains=disease_name))
        other_diseases = Disease.objects.all().exclude(name__contains=disease_name)
        title = disease.name.upper()
        return render(request, 'diseases.html', {'disease': disease, 'title':title,'other_diseases':other_diseases})
    except Disease.DoesNotExist:
        error_message = "This disease does not exit on our database"
        return render(request, 'not-found-page.html', {'error_message': error_message})

