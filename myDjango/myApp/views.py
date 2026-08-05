from django.shortcuts import redirect, render

from .forms import MovieForm, UserRegistrationForm
from .models import Movies, WatchList
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



# Create your views here.
def movie(request):
    movies = Movies.objects.all()
    return render(request, 'myApp/movie.html', {'movies': movies})


@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    in_watchlist = WatchList.objects.filter(user=request.user, movie=movie).exists()
    return render(request, 'myApp/movie_detail.html', {'movie': movie, 'in_watchlist': in_watchlist})


@login_required
def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    WatchList.objects.get_or_create(user=request.user, movie=movie)
    return redirect('watchlist')

@login_required
def watchlist(request):
    watchlist_movies = Movies.objects.filter(watchlist_entries__user=request.user).distinct()
    return render(request, 'myApp/watchlist.html', {'watchlist_movies': watchlist_movies})
@login_required
def remove_from_watchlist(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    WatchList.objects.filter(user=request.user, movie=movie).delete()
    return redirect('watchlist')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('movie')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
