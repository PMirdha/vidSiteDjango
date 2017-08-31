# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AudioTrackDetail(models.Model):
	"""docstring for AudioDetai"""
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
		return User.objects.get(pk=self.user_id).name

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
		return User.objects.get(pk=self.user_id).name +" "+ slef.order_description





#class TransDetail(models.Model):
	"""docstring for TransactionDetail"""


		
		
		
		