from django.shortcuts import render, redirect

from .models import User,Product,Order

def home(request):
    return render(request,"home.html")

def users(request):
    data = User.objects.all()
    return render(request,'showuser.html',{'data':data})

def products(request):
    data = Product.objects.all()
    return render(request,'showproducts.html',{'data':data})

def orders(request):
    data = Order.objects.all()
    return render(request,'showorders.html',{'data':data})

def deleteuser(request):
    User.objects.all().delete()
    return redirect('/')

def deleteproducts(request):
    Product.objects.all().delete()
    return redirect('/')

