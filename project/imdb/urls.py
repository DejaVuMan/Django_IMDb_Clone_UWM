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
    path('movies/<query>', views.movies_search),
    path('lists', views.all_user_movies_list),
]
