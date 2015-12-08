from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext

from users.models import User

#from users.forms import UserForm

def hello(request):
        return HttpResponse("Hello World")

def home(request):
	return render(request, 'index.html')

#def register(request):
#	form = UserForm(request.POST)
#	return render_to_response('register.html',locals(),context_instance=RequestContext(request))

#def your_name(request):
#	return render(request, 'register.html')

