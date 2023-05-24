from django.shortcuts import render
from .models import Product

# Create your views here.


def get_product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product':product
    }
    return render(request,'store/product_detail.html',context)
    