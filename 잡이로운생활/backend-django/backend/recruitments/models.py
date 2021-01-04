from django.db import models
from django.conf import settings
# from articles.models import Article

# Create your models here.
class Recruitment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    division = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    startdate = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    applicants = models.ManyToManyField("articles.Article", related_name='applicants_set', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Introduction(models.Model):
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=100)