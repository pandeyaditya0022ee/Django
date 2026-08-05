from django import forms
from .models import Movies, Genre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'date_added', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')