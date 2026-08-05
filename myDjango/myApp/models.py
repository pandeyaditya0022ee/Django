from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posters/')
    date_added = models.DateTimeField(default = timezone.now)
    genres = models.ManyToManyField(Genre, blank=True)
    rating = models.FloatField(default=0.0)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(default='No description available')

    def __str__(self):
        return self.name
