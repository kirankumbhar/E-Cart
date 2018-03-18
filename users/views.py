from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from products import views
# Create your views here.
def login(request):
	template = loader.get_template('users/login.html')
	if request.method=='POST':
		#chcek login
		username=request.POST['username']
		password=request.POST['password']
		try:
			user = User.objects.get(username=username, password=password)
		except Exception as e:
			user=None
		print(user)
		if user is not None:
			return redirect('/')
		else:
			return render(request,'users/login.html')		
	else:
		return render(request,'users/login.html')