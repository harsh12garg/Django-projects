from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def receipes(request):
    if request.method=="POST":
        data=request.POST
        
        receipe_image=request.FILES['receipe_image']
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_description=receipe_description,
            receipe_name=receipe_name
            
        )
        return redirect('/receipes/')
    
    queryset=Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'receipes':queryset}
        
    return render(request,'receipes.html',context)
    
def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    
    if request.method=="POST":
        data=request.POST
        
        receipe_image=request.FILES['receipe_image']
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        if receipe_image:
         queryset.receipe_image=receipe_image
         
        queryset.save()
        return redirect('/receipes/')
        
        
        
    context={'receipes': queryset}
    return render(request,'update_receipe.html',context)
    
    
def login_page(request):
    return render(request,'login.html')

def register(request):
    
    #authentication in django
    
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,   
        )
        user.set_password(password)
        user.save()
        
        messages.info(request,'Account created successfully')
        
        
        
        return redirect('/register/')
        
        
    
    return render(request,'register.html')