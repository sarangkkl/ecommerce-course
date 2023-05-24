from django.shortcuts import render
from store.models import Product, Category

# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')

    context = {
        'products': products,

    }
    return render(request, 'home/index.html', context)
