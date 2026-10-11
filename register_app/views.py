from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from post_app.models import Article, Comment
from .models import Profile
from .forms import RegisterForm

# context = {'errors':[]}

# def register_user(request):
#     if request.user.is_authenticated == True :
#         return redirect('/')
#     if request.method == 'POST' :
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         email = request.POST.get('email')
#         if password1 != password2 :
#             context['errors'].clear()
#             context['errors'].append('Passwords do not match')
#             print(context)
#             return render(request, 'register_app/register.html',context)
#         user=User.objects.create(username=username , password = password1 , email=email)
#         Profile.objects.create(user=user)
#         login(request, user)
#         return redirect('/')
#     return render(request,'register_app/register.html')

def register_user(request):
    if request.method=="POST":
        form = RegisterForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 =form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
                return render(request, 'register_app/register.html', {'form': form})
            if password1 != password2:
                form.add_error('password2', 'Passwords do not match.')
                return render(request, 'register_app/register.html', {'form': form})
            user = User.objects.create(username=username,password=password1,email=email)
            Profile.objects.create(user=user)
            # login(request,user)
            return redirect('/login')
        else:
            return render (request , 'register_app/register.html',{'form':form})
    elif request.method == "GET":
        form = RegisterForm()
        return render (request , 'register_app/register.html',{'form':form})


@login_required(login_url='/login/')
def user_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        if request.FILES.get('image'):
            profile.image = request.FILES['image']
            profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('user_profile')

    articles_count = Article.objects.filter(author=request.user).count()
    comments_count = Comment.objects.filter(user=request.user).count()

    return render(request, 'register_app/profile.html', {
        'profile': profile,
        'articles_count': articles_count,
        'comments_count': comments_count,
    })
