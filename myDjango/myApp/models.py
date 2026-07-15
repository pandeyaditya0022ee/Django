from django.db import models
from django.utils import timezone

# Create your models here.

class Movies(models.Model):
    genre_choices = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('Animation', 'Animation'),
        ('Documentary', 'Documentary'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Musical', 'Musical'),
        ('War', 'War'),
        ('Western', 'Western'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posters/')
    date_added = models.DateTimeField(default = timezone.now)
    genre = models.CharField(max_length=100, choices=genre_choices)
    description = models.TextField(default='No description available')

    def __str__(self):
        return self.name
