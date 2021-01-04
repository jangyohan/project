from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie
from .models import M_data
from .models import Best_Review



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class M_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = M_data
        fields = '__all__'



class Best_ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Best_Review
        fields = '__all__'



