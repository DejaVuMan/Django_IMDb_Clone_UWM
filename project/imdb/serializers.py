from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    model = People
    fields = ['name', 'age', 'date_of_birth', 'birth_location', 'bio']


class MovieSerializer(serializers.ModelSerializer):
    model = Movie
    fields = '__all__'


class UserMoviesListSerializer(serializers.ModelSerializer):
    model = UserMoviesList
    fields = '__all__'

