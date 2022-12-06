from django.contrib import admin
from .models import User, UserMoviesList
# Register your models here.

admin.site.register(User)
admin.site.register(UserMoviesList)