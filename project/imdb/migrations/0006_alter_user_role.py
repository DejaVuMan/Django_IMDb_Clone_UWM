# Generated by Django 4.1.2 on 2022-12-06 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'User'), (1, 'Admin')], default=0),
        ),
    ]