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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(_('admin_access/'), admin.site.urls),
    path('', index),
    path('home/', home),
    path(_('objectives/'), objectives),
    # path('diseases/drpla/', diseases_drpla),
    # path('diseases/hd/', diseases_hd),
    # path('diseases/sbma/', diseases_sbma),
    # path('diseases/sca1/', diseases_sca1),
    # path('diseases/sca2/', diseases_sca2),
    # path('diseases/sca3/', diseases_sca3),
    # path('diseases/sca6/', diseases_sca6),
    # path('diseases/sca7/', diseases_sca7),
    # path('diseases/sca17/', diseases_sca17),
    path(_('contact/'), contact),
    path(_('authors/'), authors),
    path(_('appreciation/'), appreciation),
    path(_('disease_search/'), search_disease, name='disease_search'),
    path(_('disease/'), tmp_disease)
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns (
    path('', index),
    path('home/', home),
    path(_('objectives/'), objectives, name="objectives"),
    # path('diseases/drpla/', diseases_drpla),
    # path('diseases/hd/', diseases_hd),
    # path('diseases/sbma/', diseases_sbma),
    # path('diseases/sca1/', diseases_sca1),
    # path('diseases/sca2/', diseases_sca2),
    # path('diseases/sca3/', diseases_sca3),
    # path('diseases/sca6/', diseases_sca6),
    # path('diseases/sca7/', diseases_sca7),
    # path('diseases/sca17/', diseases_sca17),
    path(_('contact/'), contact, name='contact'),
    path(_('authors/'), authors, name='authors'),
    path(_('appreciation/'), appreciation, name='appreciation'),
    path(_('disease_search/'), search_disease, name='disease_search'),
    path(_('disease/'), tmp_disease)
)

handler404 = 'polyQ.views.custom_page_not_found_view'
handler500 = 'polyQ.views.custom_error_view'
