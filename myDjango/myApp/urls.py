from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.movie, name='movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('watchlist/add/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/remove/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('register/',views.register,name='register')
    

]
