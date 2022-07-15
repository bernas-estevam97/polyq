from django.shortcuts import render


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
