from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Movie, UserMoviesList, People
from .serializers import UserSerializer, UserMoviesListSerializer, MovieSerializer, PeopleSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
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


@login_required()
@api_view(['PUT'])
def user_update(request, pk):
    if request.method == 'PUT':
        if request.user.pk == pk:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@login_required()
@api_view(['DELETE'])  # TODO: Authorization process
def user_delete(request, pk):
    if request.method == 'DELETE':
        if request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied


@api_view(['GET'])
def user_movies_list_get(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        movies = UserMoviesList.objects.filter(user_created=user)
        serializer = UserMoviesListSerializer(movies, many=True)
        return Response(serializer.data)


@login_required()
@api_view(['POST'])
def user_movies_list_create(request):
    if request.method == 'POST':
        serializer = UserMoviesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required()
@api_view(['PUT'])
def user_movies_list_update(request, pk, mk):
    if request.method == 'PUT':  # get the thing
        if request.user.pk == pk:  # verify user requesting to modify specific list belonging to user of PK is the same as his own PK
            user_movies_list = UserMoviesList.objects.get(pk=mk,
                                                          user_created=pk)  # get UserMoviesList object with id PK and user_created = pk
            serializer = UserMoviesListSerializer(user_movies_list, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@login_required()
@api_view(['DELETE'])
def user_movies_list_delete(request, pk, mk):
    if request.method == 'DELETE':
        if request.user.pk == pk:
            user_movies_list = UserMoviesList.objects.get(pk=mk, user_created=pk)
            user_movies_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            user_movies_list = UserMoviesList.objects.get(pk=mk)
            user_movies_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied


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


@login_required()
@api_view(['POST'])
def movie_create(request):
    if request.method == 'POST':
        if request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@login_required()
@api_view(['PUT'])
def movie_update(request, pk):
    if request.method == 'PUT':
        if request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@login_required()
@api_view(['DELETE'])
def movie_delete(request, pk):
    if request.user.groups.filter(name='Model_Admin').exists() \
            or request.user.groups.filter(name='Super_Admin').exists():
        if request.method == 'DELETE':
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        raise PermissionDenied


@api_view(['GET'])
def movie_detail(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def people_list(request):
    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def people_detail(request, pk):
    if request.method == 'GET':
        people = People.objects.get(pk=pk)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)


@login_required()
@api_view(['POST'])
def people_create(request):
    if request.method == 'POST':
        if request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            serializer = PeopleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@login_required()
@api_view(['PUT'])
def people_update(request, pk):
    if request.method == 'PUT':
        if request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            people = People.objects.get(pk=pk)
            serializer = PeopleSerializer(people, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@login_required()
@api_view(['DELETE'])
def people_delete(request, pk):
    if request.method == 'DELETE':
        if request.user.groups.filter(name='Model_Admin').exists() \
                or request.user.groups.filter(name='Super_Admin').exists():
            people = People.objects.get(pk=pk)
            people.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied
