from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
# Create your views here.

def user_login(request):
    if request.user.is_authenticated  :
        return redirect(reverse('home_page'))
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if  user != None :
            login(request,user)
            return redirect(reverse('home_page'))
    return render(request,'login_app/login.html') 

def user_logout(request):
    logout(request)
    return redirect('login')