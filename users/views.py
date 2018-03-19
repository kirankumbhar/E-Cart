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
		if user is not None:
			request.session['username']=username
			print(request.session['username'])
			return redirect('/')
		else:
			return render(request,'users/login.html')		
	else:
		return render(request,'users/login.html')

def logout(request):
	if 'username' in request.session:
		del request.session['username']
		return redirect('/')
	else:
		return redirect('/')

def user_profile(request):
	template='users/user_profile.html'
	if 'username' in request.session:
		user = User.objects.get(username=request.session['username'])
		context={
		'firstname':user.first_name,
		'lastname':user.last_name,
		'email':user.email,
		'joining_date':user.date_joined,
		}
		return render(request,template,context)
	else:
		return redirect('/')
