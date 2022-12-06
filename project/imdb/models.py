from django.db import models

# Create your models here.


class UserMoviesList(models.Model):

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
        type = models.CharField(
            max_length=15,
            choices=TYPE_OF_LIST,
            default=OTHER
    )
        is_public = models.BooleanField(default=True)


class User(models.Model):

    class Roles(models.IntegerChoices):
        USER = 0
        ADMIN = 1

    first_name = models.CharField(max_length=33)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.IntegerField(choices=Roles.choices, default=Roles.USER)
    film_lists = models.ForeignKey(UserMoviesList, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


