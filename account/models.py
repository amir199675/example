from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import (
	BaseUserManager , AbstractBaseUser , AbstractUser
)



class MyUser(AbstractUser):
	phone_number = models.CharField(max_length=11,unique=True)
	national_number = models.CharField(max_length=11,unique=True)
	city = models.CharField(max_length=32)
	province = models.CharField(max_length=32)
	location = models.CharField(max_length=64)


	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['username','email']

