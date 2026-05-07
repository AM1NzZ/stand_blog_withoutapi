from django.shortcuts import render, get_object_or_404, redirect
from .models import Article ,Category
from post_app.models import Article ,Category


# Create your views here.
def post_detail(request,title):
    article = get_object_or_404(Article,title = title)
    category = Category.objects.all()
    # if request.user.is_authenticated:
    #     return render(request,'post_app/post-details.html',{'article':article , 'category':category})
    if not request.user.is_authenticated:
        return render(request, 'home_app/login_required.html')
    return redirect('login')