# -*- coding: utf-8 -*-
#from __future__ import unicode_literalsfrom
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic,View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.forms.formsets import formset_factory
from .models import * #AudioTrackGenre,OrderDetail,UserExtraDetail,AudioTrackDetail
from .forms import * #UserRegistrationForm,AudioGenreForm,TrackDetailForm,LoginForm,LinkForm

# Create your views here.

def indexView(request):
	context={}
	s=request.session
	if('ordered_tracks' in s):
		del s['ordered_tracks']
		del s['tracks_name']
		#del s['order_choosen']
		s.modified=True
	return render(request,'audio/index.html',context)


"""**********************START Order Related**************************"""
class CreateOrderView(View):
	audio_track_genre=AudioTrackGenre.objects.all()

	def get(self,request):
		context={}
		s=request.session
		if request.GET.get('item_id') is None:
			context={'audio_track_genre':self.audio_track_genre}
			return render(request,'audio/select_order.html',context)
		else:
			item_id=request.GET.get('item_id').strip()
			item_title=request.GET.get('item_title').strip()
			#item_id=int(item_id)
			if(AudioTrackDetail.objects.filter(pk=item_id).exists()):
				if ('ordered_tracks' not in s):
					s['ordered_tracks']={}
					s['tracks_name']={}
				if(item_id not in s['ordered_tracks']):
					s['ordered_tracks'][item_id]=1
					s['tracks_name'][item_id]=item_title
					print(item_id)
				else:
					s['ordered_tracks'][item_id]+=1
					#print("\nsl;akfjl;skafj"+str(s['ordered_tracks'][item_id]))
				s.modified=True
				return HttpResponse(item_id)
			else:
				return redirect("audio:index_view")

	def post(self,request):
		context={}
		if('ordered_tracks' in request.session):
			request.session['order_choosen']=1
			request.session.modified=True
			if(request.user.username):
				return HttpResponseRedirect(reverse('audio:order_detail_view'))
			else:
				msg="Kindly login/register. You will be redirected to see your order."
				messages.add_message(request,messages.INFO,msg)
				print("Order choosen and redirecting to login")
				return redirect('audio:login_view')
		else:
			context={'audio_track_genre':self.audio_track_genre}
			print("Order choosen and redirecting to login")
			return render(request,'audio/select_order.html',context)


class OrderDetailView(generic.DetailView):
	context={}
	form=[]
	def get(self,request):
		self.form=[]
		s=request.session
		if 'ordered_tracks' in s:
			itid_vals=s['ordered_tracks'].keys()
			#return HttpResponse(itid_vals)
			for val in itid_vals:
				#print(val)
				self.form.append({'quantity':s['ordered_tracks'][val],'item_id':val,'item_title':s['tracks_name'][val]})
			self.context={'form':self.form}
			return render(request,'audio/order_detail.html',self.context)
		else:
			messages.add_message(request,messages.INFO,"Place an order first")
			return redirect("audio:index_view")

	def post(self,request):
		self.context={}
		track_detail=AudioTrackDetail.objects
		user=request.user
		order=OrderDetail()
		order.user_id=user
		order.total_item=len(self.form)
		order.order_description="Nothing right now"
		order.total_amount=0
		order.delivered_flag=False
		order.cancelled_flag=False
		order.save()
		tamount=0
		for field in self.form:
			item_id=field['item_id']
			print(item_id)
			quantity=int(field['quantity'])
			atd=track_detail.get(pk=item_id)
			price=atd.price
			tamount+=(quantity*price)
			item_detail=OrderItemDetail()
			item_detail.audio_track_detail=atd
			item_detail.ordered_tracks=order
			item_detail.quantity=quantity
			item_detail.amount=(quantity*price)
			item_detail.save()
		order.total_amount=tamount
		order.save()
		s=request.session
		if('ordered_tracks' in s):
			del s['ordered_tracks']
			del s['tracks_name']
		s.modified=True
		return redirect('audio:index_view')
"""************************END Order Related**************************"""

"""************************START Populate Table Data***********************"""

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
"""************************END Populate Table Data***********************"""


"""******************START Registration, Login and Logout**********************"""

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
			username,x=form.cleaned_data['email'].split('@')
			print(user.username)
			password=form.cleaned_data['password']
			user.email=form.cleaned_data['email']
			user.username=username
			user.set_password(password)
			user.save()

			extra_detail=UserExtraDetail()
			extra_detail.user_id=user
			extra_detail.user_name=form.cleaned_data['username']
			extra_detail.mobile_no=form.cleaned_data['mobile_no']
			extra_detail.address=form.cleaned_data['address']
			extra_detail.save()
			"""Authenticate and log in the user"""
			user=authenticate(username=username,password=password)
			login(request,user)

			if user is not None:
				msg=extra_detail.user_name+" have been successfully Rgistered"
				messages.add_message(request,messages.INFO,msg)
				if 'ordered_tracks' in request.session:
					return redirect("audio:order_detail_view")
				else:
					return redirect('audio:index_view')
		else :
			return render(request,self.template_name,{'form':form})

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
					if user.username:
						msg=user.username+" have been successfully logged in"
						messages.add_message(request,messages.INFO,msg)
					login(request,user)
					if 'ordered_tracks' in request.session:
						return redirect("audio:order_detail_view")
					else:
						return redirect("audio:index_view")

		return render(request,self.template_name,{'form':form})

class LogoutView(View):

	def get(self,request):
		username=request.user.username
		if username:
			msg=username+" have been successfully logged out"
			messages.add_message(request,messages.INFO,msg)
		logout(request)
		return redirect("audio:index_view")

"""******************END Registration, Login and Logout**********************"""








		