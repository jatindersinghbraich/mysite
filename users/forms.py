from django import forms
from django.forms import ModelForm

from .models import User

#class UserForm(forms.Form):
#	first_name = forms.CharField(label='First name', max_length=30)
#	last_name = forms.CharField(label='Last name', max_length=30)
#	disp_name = forms.CharField(label='Display name', max_length=30)
#	email_id = forms.EmailField(label='Email ID', max_length=30)
#	password = forms.CharField(label='Password', max_length=30)

#class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)

class UserForm(ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	disp_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email_id = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = [ 'first_name','last_name','disp_name','email_id','password']