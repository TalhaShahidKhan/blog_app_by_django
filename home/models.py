from django.db import models
from django.contrib.auth.models import AbstractUser
from home.manage import UserManager
# Create your models here.


class CustomUser(AbstractUser):
  bio=models.TextField(blank=True)
  pic=models.ImageField(null=True ,upload_to='profile/images',blank=True)
  address=models.CharField(max_length=200, blank=True)
  profession=models.CharField(max_length=200,blank=True)

  object=UserManager()

  USERNAME_FIELD="username"
  REQUIRED_FIELDS=[]
