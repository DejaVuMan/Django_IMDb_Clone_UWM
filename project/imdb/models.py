from django.db import models

# Create your models here.
class User(models.Model):

    class Roles(models.IntegerChoices):
        USER = 0
        ADMIN = 1

    first_name = models.CharField(max_length=33)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.IntegerField(choices=Roles.choices, default=Roles.USER)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
