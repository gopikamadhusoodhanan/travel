from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        User=auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def reg(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        e_mail=request.POST['e_mail']
        password=request.POST['password']
        cpassword=request.POST['pass']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User Taken")
                return redirect('reg')
            elif User.objects.filter(email=e_mail).exists():
               messages.info(request,"Email Taken")
               return redirect('reg')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=e_mail,password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password not Matching")
            return redirect('reg')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
