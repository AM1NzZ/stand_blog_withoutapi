from django.shortcuts import render, get_object_or_404, redirect
from .models import Article ,Category
from post_app.models import Article ,Category ,ArticleManager


# Create your views here.
def post_detail(request,title):
    # article = Article.objects.published(title = title)
    article = get_object_or_404(Article,title = title)
    category = Category.objects.all()
    if request.user.is_authenticated:
        return render(request,'post_app/post-details.html',{'article':article , 'category':category})
    elif not request.user.is_authenticated:
        return render(request, 'home_app/login_required.html')
    return redirect('login')
def sort_article_by_category(request , category):
    articles = Article.objects.filter(category__title = category)
    print(articles)
    return render(request,"post_app/category.html" ,{'articles':articles,"category":category})
def blog_entries(request):
    articles = Article.objects.all()
    return render(request,'post_app/blog-entries.html',{'articles':articles})