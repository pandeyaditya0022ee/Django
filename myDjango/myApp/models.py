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
    trailer_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='watchlist_items')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='watchlist_entries')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-added_at']

    def __str__(self):
        return f'{self.user.username} - {self.movie.name}'
