from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# Create your views here.

context = {'errors':[]}
def register_user(request):
    if request.user.is_authenticated == True :
        return redirect('/')
    if request.method == 'POST' :
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 != password2 :
            context['errors'].clear()
            context['errors'].append('Passwords do not match')
            print(context)
            return render(request, 'register_app/register.html',context)
        # if User.objects.get(username = username):
        #     context['errors'].append('Username already exists')
        #     return render(request, 'register_app/register.html',context)
        user=User.objects.create(username=username , password = password1 , email=email)
        login(request, user)
        return redirect('/')
    return render(request,'register_app/register.html')