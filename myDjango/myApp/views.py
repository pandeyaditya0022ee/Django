from django.shortcuts import redirect, render

from .forms import MovieForm, UserRegistrationForm
from .models import Movies
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
    return render(request, 'myApp/movie_detail.html', {'movie': movie})



@login_required    
def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

@login_required
def movie_edit(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id, user = request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie')
    else:
        form = MovieForm(instance=movie)
        
    return render(request, 'movie_form.html', {'form': form})

@login_required
def movie_delete(request,movie_id):
    movie = get_object_or_404(Movies, pk=movie_id, user = request.user)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})




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
