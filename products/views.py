from django.shortcuts import render_to_response, redirect, get_object_or_404
from products.models import Product, ProductForm
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test

def home(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render_to_response('home.html', { 'products': products}, RequestContext(request))

def productid(request, id):
    product = Product.objects.get(id = id)
    return render_to_response("productid.html", { 'product' : product,}, RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def productedit(request, id):
    product = get_object_or_404(Product, id = id)
    form = ProductForm(request.POST or None, request.FILES or None, instance = product)
    if form.is_valid():
        form.save()
        return redirect('/id'+id) 
    form = ProductForm(instance = product)
    return render_to_response("edit.html", {'form' : form, 'id' : id,}, RequestContext(request))