from django.contrib import admin
from .models import Movies, Genre
# Register your models here.

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
	filter_horizontal = ('genres',)


admin.site.register(Genre)
