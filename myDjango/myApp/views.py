from django.shortcuts import render
from .models import Movies
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    movies = Movies.objects.all()
    return render(request, 'myApp/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    return render(request, 'myApp/movie_detail.html', {'movie': movie})