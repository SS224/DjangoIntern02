from django.shortcuts import render
from appOne.models import Product
from appOne.forms import ProductForm
from django.http import HttpResponseRedirect
# Create your views here.

def getProducts(request):

    products = Product.objects.all()
    return render(request, 'templates/index.html', {'products': products})

def updateProduct(request, id):

    product = Product.objects.get(id=id)

    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'templates/updateProduct.html', {'form':form})

//createProduct
//deleteProduct
