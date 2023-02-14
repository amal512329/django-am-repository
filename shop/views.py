from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def register(request):
    return render(request,'shop/register.html')

def collections(request):
    category = Catagory.objects.filter(status=0)
    return render(request,'shop/collections.html',{'category':category})

def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
      products=Product.objects.filter(category__name=name)
      return render(request,"shop/products/index.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('collections')


def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')