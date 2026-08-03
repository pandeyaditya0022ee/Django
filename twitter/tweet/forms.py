from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'photo']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
        }