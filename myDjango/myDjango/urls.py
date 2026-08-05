"""
URL configuration for myDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.movie, name='movie')
Class-based views
    1. Add an import:  from other_app.views import movie
    2. Add a URL to urlpatterns:  path('', movie.as_view(), name='movie')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index

from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('myApp/', include('myApp.urls')),
    path("accounts/", include('django.contrib.auth.urls')),



    path("__reload__/", include("django_browser_reload.urls")), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
