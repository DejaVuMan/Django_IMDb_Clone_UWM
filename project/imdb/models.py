from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class People(models.Model):
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    birth_location = models.CharField(max_length=100)
    bio = models.TextField()


class Movie(models.Model):
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    ANIMATED = 'Animated'
    COMEDY = 'Comedy'
    DRAMA = 'Drama'
    FANTASY = 'Fantasy'
    HISTORICAL = 'Historical'
    HORROR = 'Horror'
    MUSICAL = 'Musical'
    ROMANCE = 'Romance'
    SCIENCE_FICTION = 'Science Fiction'
    THRILLER = 'Thriller'
    WESTERN = 'Western'
    OTHER = 'Other'

    TYPE_OF_LIST = [
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (ANIMATED, 'Animated'),
        (COMEDY, 'Comedy'),
        (DRAMA, 'Drama'),
        (FANTASY, 'Fantasy'),
        (HISTORICAL, 'Historical'),
        (HORROR, 'Horror'),
        (MUSICAL, 'Musical'),
        (ROMANCE, 'Romance'),
        (SCIENCE_FICTION, 'Science Fiction'),
        (THRILLER, 'Thriller'),
        (WESTERN, 'Western'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    director = models.ForeignKey(People, on_delete=models.CASCADE, related_name='director')
    genre = models.CharField(max_length=100, choices=TYPE_OF_LIST, default=OTHER)
    rating = models.FloatField(default=0.0)
    cast = models.ManyToManyField(People, related_name='cast')


class UserMoviesList(models.Model):
    class Meta:
        verbose_name = 'User Film List'
        verbose_name_plural = 'User Film Lists'

    # TODO: It might get repetitive to have to keep on adding these lists to models, look into mixin viability
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    ANIMATED = 'Animated'
    COMEDY = 'Comedy'
    DRAMA = 'Drama'
    FANTASY = 'Fantasy'
    HISTORICAL = 'Historical'
    HORROR = 'Horror'
    MUSICAL = 'Musical'
    ROMANCE = 'Romance'
    SCIENCE_FICTION = 'Science Fiction'
    THRILLER = 'Thriller'
    WESTERN = 'Western'
    OTHER = 'Other'

    TYPE_OF_LIST = [
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (ANIMATED, 'Animated'),
        (COMEDY, 'Comedy'),
        (DRAMA, 'Drama'),
        (FANTASY, 'Fantasy'),
        (HISTORICAL, 'Historical'),
        (HORROR, 'Horror'),
        (MUSICAL, 'Musical'),
        (ROMANCE, 'Romance'),
        (SCIENCE_FICTION, 'Science Fiction'),
        (THRILLER, 'Thriller'),
        (WESTERN, 'Western'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    genre = models.CharField(
        max_length=15,
        choices=TYPE_OF_LIST,
        default=OTHER
    )

    movies = models.ManyToManyField(Movie, related_name='movies', blank=True)

    is_public = models.BooleanField(default=True)


class User(AbstractUser):
    class Roles(models.IntegerChoices):
        USER = 0
        ADMIN = 1

    # default fields from User are already passed here
    first_name = models.CharField(max_length=33)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    role = models.IntegerField(choices=Roles.choices, default=Roles.USER)
    film_lists = models.ForeignKey(UserMoviesList, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
