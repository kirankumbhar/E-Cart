from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Products
# Create your views here.
def index(request):
	#homepage of website
	all_products = Products.objects.raw("select * from products")
	context = {
	 'products':all_products,
	}
	return render(request,'products/index.html',context)


