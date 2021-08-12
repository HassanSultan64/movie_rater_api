from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator , MinValueValidator

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)


