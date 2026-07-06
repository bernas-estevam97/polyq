"""polyQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('access_django_adm/', admin.site.urls),
    path('', index, name="landing_page"),
    path('home', home, name="home_page"),
    path('objectives', objectives, name="objectives"),
    path('contact', contact, name='contact_page'),
    path('authors', authors, name="authors"),
    path('appreciation', appreciation, name="thanks"),
    path('disease_search/', search_disease, name='disease_search'),
    path('support', support, name='support'),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)


handler404 = 'polyQ.views.custom_page_not_found_view'
handler500 = 'polyQ.views.custom_error_view'
