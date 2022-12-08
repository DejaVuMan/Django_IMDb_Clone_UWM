from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Movie, UserMoviesList
from .serializers import UserSerializer, UserMoviesListSerializer, MovieSerializer, PeopleSerializer
from django.core.exceptions import PermissionDenied


@api_view(['GET'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) # TODO: Authorization process
def user_update(request, pk):
    if request.method == 'PUT':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) # TODO: Authorization process
def user_delete(request, pk):
    if request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_movies_list(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        movies = user.film_lists
        list_ids = UserMoviesList.objects.get(pk=movies.id)
        serializer = UserMoviesListSerializer(list_ids, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def all_user_movies_list(request):
    if request.method == 'GET':
        movies = UserMoviesList.objects.all()
        serializer = UserMoviesListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movies_search(request, query):
    if request.method == 'GET':
        movies = Movie.objects.filter(title__icontains=query)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

