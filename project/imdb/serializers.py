from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'age', 'date_of_birth', 'birth_location', 'bio']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class UserMoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMoviesList
        fields = '__all__'

