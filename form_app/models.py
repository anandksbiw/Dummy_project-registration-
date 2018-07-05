from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    address = models.CharField(max_length = 100, blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True,null=True)
    resume = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class librarydue(models.Model):
    roll=models.CharField(primary_key=True,max_length=20)
    dues=models.IntegerField()


