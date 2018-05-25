from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from products import views
from django.contrib import messages
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

def register(request):
	template='users/register.html'
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		count = User.objects.filter(username=username).count()
		print(count)
		if(count>0):
			context={
			'error':'username already exists!',
			}
			return render(request,template,context)
		else:
			register = User(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
			register.save()
			messages.success(request, 'Profile created.')
			context={
				'success':'Profile created successfully',
			}
			#register = User.objects.raw('insert into(first_name,last_name,email,username,password) auth_user values(%s,%s,%s,%s,%s)',[first_name,last_name,email,username,password])
			return render(request,template,context)
	else:
		return render(request,template)