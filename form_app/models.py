from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    name= models.CharField(max_length=30)
    address = models.CharField(max_length = 100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    resume = models.URLField(blank=True)

    def __str__(self):
        return self.user.name



