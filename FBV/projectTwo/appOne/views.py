from django.shortcuts import render
from appOne.models import Product
from appOne.forms import ProductForm
# Create your views here.

def getProducts(request):

    products = Product.objects.all()
    return render(request, 'templates/index.html', {'products': products})
