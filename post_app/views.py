from django.shortcuts import render,get_object_or_404
from .models import Article ,Category
from post_app.models import Article


# Create your views here.
def post_detail(request,title):
    article = get_object_or_404(Article,title = title)
    return render(request,'post_app/post-details.html',{'article':article})
