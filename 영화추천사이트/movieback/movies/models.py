from django.db import models
from django.conf import settings
import os
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    pubDate = models.IntegerField()
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    userRating = models.FloatField(max_length=100)
    key_id = models.IntegerField()


class M_data(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post = models.CharField(max_length=10000)
    score = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

class Best_Review(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField()
    director = models.CharField(max_length=100)

class MovieData(models.Model):
    movieCd = models.CharField(max_length=10000, default='null')
    movieNm = models.CharField(max_length=10000, default='null')
    movieNmEn =  models.CharField(max_length=10000, default='null')
    prdtYear = models.CharField(max_length=10000, default='null')
    openDt = models.CharField(max_length=10000, default='null')
    typeNm = models.CharField(max_length=10000, default='null')
    prdtStatNm = models.CharField(max_length=10000, default='null')
    nationAlt = models.CharField(max_length=10000, default='null')
    genreAlt = models.CharField(max_length=10000, default='null')
    repNationNm = models.CharField(max_length=10000, default='null')
    repGenreNm = models.CharField(max_length=10000, default='null')
    directors = models.CharField(max_length=10000, default='null')
    companys = models.CharField(max_length=10000, default='null')