from django.db import models
#from django.forms import ModelForm

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	display_name = models.CharField(max_length=30)
	email_id = models.EmailField(max_length=30)
	password = models.CharField(max_length=30)
	
	def __str__(self):
		return self.first_name

#class UserForm(ModelForm):
#	class Meta:
#		model = User
#		fields = ['first_name','last_name','display_name','email_id','password']

