from django.shortcuts import render
from .models import*
from django.core.paginator import Paginator
# Create your views here.
def product(request):
    prod=Product.objects.all()
    pag = Paginator(Product.objects.all(),12)
    page = request.GET.get('page')
    venues = pag.get_page(page)
    context={
        'product':prod,
        'product':venues
    }
    return render(request,'Products.html',context)

def viewdetails(request,c_slug,product_slug):
    try:
        prod=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    context={
        'product':prod
    }
    return render(request,'view.html',context)