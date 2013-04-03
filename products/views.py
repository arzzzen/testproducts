from django.shortcuts import render_to_response
from products.models import Product

def home(request):
    products = Product.objects.all()
    return render_to_response("home.html", { 'products' : products,})

def productid(request, id):
    product = Product.objects.get(id = id)
    return render_to_response("productid.html", { 'product' : product,})