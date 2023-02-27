from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
  bio=models.TextField(blank=True)
  pic=models.ImageField(null=True ,upload_to='profile/images')
  address=models.CharField(max_length=200, blank=True)
  profession=models.CharField(max_length=200,blank=True)

