# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator



# Create your models here.
class AudioTrackGenre(models.Model):
	"""docstring for AudioTrackGenre"""
	genre_description=models.CharField(max_length=100)
	
	def __str__(self):
		return self.genre_description

class AudioTrackDetail(models.Model):
	"""docstring for AudioDetai"""
	genre = models.ForeignKey(AudioTrackGenre,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	discription = models.CharField(max_length=100)
	price = models.IntegerField()

	def __str__(self):
		return self.title

class UserExtraDetail(models.Model):
	"""docstring for TransactionDetail"""
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	mobile_no=models.IntegerField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])
	address=models.CharField(max_length=100)

	def __str__(self):
		return self.user_id.name

class OrderDetail(models.Model):
	"""docstring for OrderDetail"""
	user_id=models.ForeignKey(User)
	total_item=models.IntegerField()
	order_description=models.CharField(max_length=3000)
	order_time=models.DateField(auto_now=True)
	total_amount=models.IntegerField()
	delivered_flag=models.BooleanField()
	cancelled_flag=models.BooleanField()

	def __str__(self):
		return self.user_id.name +" "+ slef.order_description





#class TransDetail(models.Model):
	"""docstring for TransactionDetail"""


		
		
		
#from django.db import models
class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):
		return self.name
# __unicode__ on Python 2

class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.name
# __unicode__ on Python 2

class Entry(models.Model):
	blog = models.ForeignKey(Blog)
	authors = models.ManyToManyField(Author)

	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	n_comments = models.IntegerField()
	n_pingbacks = models.IntegerField()
	rating = models.IntegerField()

	def __str__(self):
		return self.headline