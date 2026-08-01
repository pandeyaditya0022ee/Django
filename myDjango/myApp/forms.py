from django import forms
from .models import Movies, Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'date_added', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }