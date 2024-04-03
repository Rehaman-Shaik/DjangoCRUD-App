from django.db import models
from .utils import movie_directory_path

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True,null=True)
    release_date = models.CharField(max_length=30,blank=True,null=True)
    rating = models.IntegerField(blank=True,null=True)
    image= models.ImageField(upload_to=movie_directory_path,blank=True,null=True)
    director = models.CharField(max_length=100,blank=True,null=True)
    language = models.CharField(max_length=50,blank=True,null=True)
    runtime = models.CharField(max_length=14,blank=True,null=True)
    
    def __str__(self):
        return self.name
    