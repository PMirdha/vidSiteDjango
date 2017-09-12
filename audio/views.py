# -*- coding: utf-8 -*-
#from __future__ import unicode_literalsfrom
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic,View
from django.contrib.auth.models import User
from .models import AudioTrackGenre,OrderDetail,UserExtraDetail
from .forms import UserRegistrationForm

# Create your views here.

def indexView(request):
	context={}
	return render(request,'audio/index.html',context)

class CreateOrderView(View):

	def get(self,request):
		audio_track_genre=AudioTrackGenre.objects.all()
		context={'audio_track_genre':audio_track_genre}
		return render(request,'audio/select_order.html',context)

	def put(self,request):
		context={}
		return render(request,'audio/select_order.html',context)


class OrderDetailView(generic.DetailView):
	template_name='audio/order_detail.html'
	model = OrderDetail




class RegistrationView(View):
	"""docstring for RegistrationView"""
	form_class=UserRegistrationForm
	template_name='audio/registration.html'

	def get(self,request):
		form=self.form_class(None)
		context={'form':form}
		return render(request,self.template_name,context)

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			print(user)
			#user=User()
			user.username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.email=form.cleaned_data['email']

			user.set_password(password)
			user.save()

			extra_detail=UserExtraDetail()
			extra_detail.user_id=user
			extra_detail.mobile_no=form.cleaned_data['mobile_no']
			extra_detail.address=form.cleaned_data['address']
			extra_detail.save()
			return HttpResponse(user) #redirect('audio:index_view')
		else :
			return HttpResponse("Not correct")














		