from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.CloudinaryField('image',blank = True)
    bio = models.TextField(max_length = 100,blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    followers = models.ManyToManyField(User,blank=True,related_name='followers')
