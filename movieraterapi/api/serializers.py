from rest_framework import serializers
from .models import Movie
from .models import Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'title']



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['name','title', 'User','stars']