from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.tweet_list, name = "tweet_list"),
    path("create/", views.tweet_create, name = "tweet_create"),
    path("<int:tweet_id>/edit/", views.tweet_edit, name = "tweet_edit"),
    path("<int:tweet_id>/delete/", views.tweet_delete, name = "tweet_delete"),
    path("register/", views.register, name = "register"),
    
    
    
    
    path('__reload__/', include('django_browser_reload.urls')),
] 
