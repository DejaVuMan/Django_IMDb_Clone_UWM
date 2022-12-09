from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, UserMoviesList, People, Movie


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'role']


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(UserMoviesList)
admin.site.register(People)
admin.site.register(Movie)
