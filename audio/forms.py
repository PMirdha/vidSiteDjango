from django import forms
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
	"""docstring for CreateOrderForm"""
	#username=forms.CharField(max_length=100)
	#email=forms.EmailField()
	mobile_no=forms.CharField(max_length=10,min_length=10,widget=forms.NumberInput(attrs={'type':'number'}))
	address=forms.CharField(max_length=100)
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		"""docstring for Meta"""
		model=User
		fields = ['username','email','password']

	def save(self, commit=False):
		return super(UserRegistrationForm, self).save(commit=commit)
			


