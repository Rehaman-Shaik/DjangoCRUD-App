from django.db import models

# Create your models here.

class Profile(models.Model):
    fname = models.CharField(max_length =100)
    lname = models.CharField(max_length =100)
    user_name = models.CharField(max_length =50)
    description = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user_name