from django.shortcuts import render_to_response
from products.models import Product
from django.template import RequestContext

def home(request):
    products = Product.objects.all()
    return render_to_response("home.html", { 'products' : products,},RequestContext(request))

def productid(request, id):
    product = Product.objects.get(id = id)
    return render_to_response("productid.html", { 'product' : product,},RequestContext(request))