from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
	template = loader.get_template('products/index.html');
	#homepage of website
	return render(request,'products/index.html')


