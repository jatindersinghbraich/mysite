from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail

from django.contrib import messages

from .models import User
#from .forms import User_Reg,NameForm

from .forms import UserForm

# Create your views here.
def user_register(request):
	#p = get_object_or_404(User)
	form = UserForm()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid :
			save_it = form.save(commit=False)
			save_it.save()
			#send_mail
			subject = 'Thank you for registration'
			message = 'Welcome to the world of jatinder'
			from_email = settings.EMAIL_HOST_USER
			to_list = [save_it.email_id]
			#send_mail(subject,from_email,to_list,fail_silently=True)
			messages.success(request,'Profile updated successfully')
			#return HttpResponseRedirect('/thanks/')
			#return render_to_response("index.html")
			return render(request,"index.html",{'form':form,'flag':'dada'})
	else:
		#return render_to_response("index.html",locals(),context_instance=RequestContext(request))
		return render(request,"register_snippet.html",{'form':form,'flag':'flag'})
def thank_you(request):

	return render_to_response("thanks.html",locals(),context_instance=RequestContext(request))

#	if request.method = 'POST':
#		form = User_Reg(request.POST)
#		if form.is_valid():
#			First_Name = form.cleaned_data['first_name']
#			Last_Name = form.cleaned_data['last_name']
   #     		Disp_Name = form.cleaned_data['display_name']
  #      		Email_Id = form.cleaned_data['email_id']
 #       		Password = form.cleaned_data['password']
#			p = User(first_name=First_Name,last_name=Last_Name,display_name=Disp_Name,email_id=Email_Id,password=Password)
#			p.save()
#			return HttpResponseRedirect('/thanks/')
#	else:
#		form = User_Reg()
#		
#	return render(request, 'index.html', {'form': form})
#
#def get_name(request):
#	if request.method = 'POST':
#		form = NameForm(request.POST)
#		if form.is_valid():
#			return HttpResponseRedirect('/thanks/')
#	else:
#		form=NameForm()
#	return render(request, 'register.html', {'form': form})
			
