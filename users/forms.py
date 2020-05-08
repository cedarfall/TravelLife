from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	
	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'email', 'password2']:
			self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']
	
	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'email']:
			self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
	website = forms.CharField(required=False)
	twitter = forms.CharField(required=False)
	linkedin = forms.CharField(required=False)
	facebook = forms.CharField(required=False)

	class Meta:
		model = Profile
		fields = ['website', 'twitter', 'linkedin', 'facebook', 'image']