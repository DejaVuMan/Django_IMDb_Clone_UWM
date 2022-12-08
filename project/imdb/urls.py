from django.urls import path

from . import views

urlpatterns = [
    path('users', views.users_list),
    path('users/<int:pk>', views.user_detail),
    path('users/create', views.user_create),
    path('users/<int:pk>/update', views.user_update),
    path('users/<int:pk>/delete', views.user_delete),
    path('users/<int:pk>/movies', views.user_movies_list),
    path('movies', views.movies_list),
    path('movies/<int:pk>', views.movie_detail),
    path('movies/create', views.movie_create),
    path('movies/<int:pk>/update', views.movie_update),
    path('movies/<int:pk>/delete', views.movie_delete),
    path('movies/<query>', views.movies_search),
]
