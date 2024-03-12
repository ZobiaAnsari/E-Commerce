from django.shortcuts import render
from django.http import HttpResponse
from .models import Product  
from math import ceil 
# Create your views here.


def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("we are in contact")

def tracker(request):
    return HttpResponse("we are in tracker")

def search(request):
    return HttpResponse("we are in search")

def productview(request):
    return HttpResponse("we are in prodview")

def checkout(request):
    return HttpResponse("we are in checkout")