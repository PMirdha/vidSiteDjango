from django import forms
from .models import AudioTrackGenre,AudioTrackDetail
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator

NumCharOnly=RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed for Mobile Number.')
#genre_list=AudioTrackGenre.objects.values_list("genre_description")
genre_list=[]
for genre in AudioTrackGenre.objects.all():
	genre_list.append((genre.pk,genre.genre_description))
#genre_list=tuple(genre_list)

class UserRegistrationForm(forms.Form):
	"""docstring for CreateOrderForm"""
	username=forms.CharField(max_length=100)
	email=forms.EmailField()
	mobile_no=forms.CharField(max_length=10,
		min_length=10,
		validators=[NumCharOnly])
	address=forms.CharField(max_length=100)
	password=forms.CharField(widget=forms.PasswordInput)
	

class AudioGenreForm(forms.ModelForm):

	class Meta:
		model=AudioTrackGenre
		fields=['genre_description']

class TrackDetailForm(forms.Form):

	genre=forms.ChoiceField(choices=genre_list)
	title = forms.CharField(max_length=100)
	discription = forms.CharField(max_length=100)
	price = forms.IntegerField()

	#class Meta:
		#model=AudioTrackDetail
		#fields=['genre','title','discription','price']

class LoginForm(forms.Form):

	username=forms.CharField(max_length=100)
	password=forms.CharField(widget=forms.PasswordInput)


