# -*- coding: utf-8 -*-
#from __future__ import unicode_literalsfrom
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic,View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import AudioTrackGenre,OrderDetail,UserExtraDetail,AudioTrackDetail
from .forms import UserRegistrationForm,AudioGenreForm,TrackDetailForm,LoginForm

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

			user=User()
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
			return redirect('audio:index_view')
		else :
			return render(request,self.template_name,{'form':form})


class GenrePopulateView(View):
	"""Can be done without much effort see
		from django.views.generic.edit import CreateView, UpdateView, DeleteView"""
	form_class=AudioGenreForm
	template_name='audio/genre_populate.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})


	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			genre=form.save()
			return redirect('audio:index_view')

		else :
			return render(request,self.template_name,{'form':form})


class TrackPopulateView(View):
	form_class=TrackDetailForm
	template_name='audio/track_populate.html'

	def get(self,request):
		form=self.form_class(None)
		user=request.user
		return render(request,self.template_name,{'form':form,'user':user})


	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			gid=form.cleaned_data['genre']
			track_detail=AudioTrackDetail()
			track_detail.genre=AudioTrackGenre.objects.get(pk=gid)
			track_detail.title=form.cleaned_data['title']
			track_detail.discription=form.cleaned_data['discription']
			track_detail.price=form.cleaned_data['price']
			track_detail.save()
			return redirect('audio:index_view')

		else :
			return render(request,self.template_name,{'form':form,'user':user})

class LoginView(View):
	form_class=LoginForm
	template_name="audio/login.html"

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:

					login(request,user)
					return redirect("audio:create_order_view")

		return render(request,self.template_name,{'form':form})











		