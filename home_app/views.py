from django.shortcuts import render , get_object_or_404
from post_app.models import Article, Category


def index_page(request):
    articles = Article.objects.all()
    # articles = Article.objects.published()
    categories=Category.objects.all()
    return render (request,'home_app/index.html',{'articles':articles , 'categories':categories})
