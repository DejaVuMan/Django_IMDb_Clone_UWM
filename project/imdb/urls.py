from django.urls import path

from . import views

urlpatterns = [
    path('users', views.users_list),
    path('users/<int:pk>', views.user_detail),
    path('users/create', views.user_create),
    path('users/<int:pk>/update', views.user_update),
    path('users/<int:pk>/delete', views.user_delete),
    path('users/<int:pk>/movielist', views.user_movies_list_get),
    path('movielist/create', views.user_movies_list_create),
    path('users/<int:pk>/movielist/<int:mk>/update', views.user_movies_list_update),
    path('movies', views.movies_list),
    path('movies/<int:pk>', views.movie_detail),
    path('movies/create', views.movie_create),
    path('movies/<int:pk>/update', views.movie_update),
    path('movies/<int:pk>/delete', views.movie_delete),
    path('movies/<query>', views.movies_search),
    path('people', views.people_list),
    path('people/<int:pk>', views.people_detail),
    path('people/create', views.people_create),
    path('people/<int:pk>/update', views.people_update),
    path('people/<int:pk>/delete', views.people_delete),

]
