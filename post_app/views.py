from django.shortcuts import render,get_object_or_404
from .models import Article ,Category
from post_app.models import Article ,Category


# Create your views here.
def post_detail(request,title):
    article = get_object_or_404(Article,title = title)
    category = Category.objects.all()
    return render(request,'post_app/post-details.html',{'article':article , 'category':category})
