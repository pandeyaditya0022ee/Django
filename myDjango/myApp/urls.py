from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.movie, name='movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add/',views.movie_add,name='movie_add'),
    path('edit/<int:movie_id>/', views.movie_edit, name='movie_edit'),
    path('delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
    path('register/',views.register,name='register')
    

]
