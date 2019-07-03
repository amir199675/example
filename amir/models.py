from django.db import models
from django.db.models.signals import post_save,pre_save
from account.models import MyUser
from django.dispatch import receiver
# Create your models here.
from polymorphic.models import PolymorphicModel

class Author (models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)
	email = models.CharField(unique=True,max_length=32)



def save_author(sender,instance,**kwargs):
	print('Author was saved')
post_save.connect(save_author,sender=Author)



class Book(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)
	type = models.CharField(max_length=32)
	author = models.ForeignKey(Author,related_name='auth',on_delete=models.CASCADE)



class Userprofile(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(MyUser,on_delete="CASCADE")
	phone_number = models.CharField(max_length=11)


	def __str__(self):
		return self.user_id.first_name





# 	if kwargs['created']:
# 		user_profile = Userprofile.objects.create(user =kwargs['instance'] )
#
# pre_save.connect(create_profile,sender=User)