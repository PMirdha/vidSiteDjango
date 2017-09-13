# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator

NumCharOnly=RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

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
	mobile_no=models.IntegerField(validators=[MaxLengthValidator(10),MinLengthValidator(10),NumCharOnly])
	address=models.CharField(max_length=100)

	def __str__(self):
		return self.user_id.username

class OrderDetail(models.Model):
	"""docstring for OrderDetail"""
	user_id=models.ForeignKey(User)
	audio_track_detail=models.ManyToManyField(AudioTrackDetail,through='OrderItemDetail')
	total_item=models.IntegerField()
	order_description=models.CharField(max_length=3000)
	order_time=models.DateField(auto_now=True)
	total_amount=models.IntegerField()
	delivered_flag=models.BooleanField()
	cancelled_flag=models.BooleanField()

	def __str__(self):
		return self.user_id.name +" "+ slef.order_description


class OrderItemDetail(models.Model):
	"""docstring for OrderItemDetail"""
	audio_track_detail=models.ForeignKey(AudioTrackDetail)
	order_detail=models.ForeignKey(OrderDetail,on_delete=models.CASCADE)
	quantity=models.IntegerField();
	amount=models.FloatField();
		



#class TransDetail(models.Model):
	"""docstring for TransactionDetail"""


		
	