from django.contrib import admin
from .models import Movies, Genre
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_added')
	filter_horizontal = ('genres',)


admin.site.register(Genre)
admin.site.register(Movies, MoviesAdmin)
