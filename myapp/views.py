from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from myapp.models import Employes

# Create your views here.

def signupPage(request):
    if request.method == "POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return redirect('/')
        else:
            user=User.objects.create_user(username=uname,email=email,password=pass1,)
            user.save()
            return redirect('loginPage')
    return render(request,'signup.html')


def loginPage(request):
    if request.method == "POST":
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(username=uname, password=pass1)
        if user!=None:
            return redirect('homePage')
        else:
            return redirect('loginPage')


    
    return render(request,'login.html')


def homePage(request):
    user=request.user
    emp=Employes.objects.all()
    return render(request,'home.html',{'emp':emp,})
