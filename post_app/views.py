from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from post_app.models import Article, Category

from django.views.generic.base import View
from django.views.generic import ListView

# Create your views here.
def post_detail(request, title):
    # article = Article.objects.published(title = title)
    article = get_object_or_404(Article, title=title)

    category = Category.objects.all()
    if request.user.is_authenticated:
        return render(request, 'post_app/post-details.html', {'article': article, 'category': category})
    elif not request.user.is_authenticated:
        return render(request, 'home_app/login_required.html')
    return redirect('login')


def sort_article_by_category(request, category):
    articles = Article.objects.published().filter(category__title=category)
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(request.GET.get('page'))
    return render(request, "post_app/blog-entries.html", {'articles': object_list, "category": category})


# def Sort_article_by_category(request, pk=None):
#     category = get_object_or_404(Category, id=pk)
#     articles = category.articles.all()
#     return render(request, "post_app/blog-entries.html", {'articles': articles, "category": category})

def blog_entries(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(request.GET.get('page'))
    return render(request, 'post_app/blog-entries.html', {'articles': object_list})


# class TestViewBase(View):
#     name = "amin"
#     def get(self,request):
#         return HttpResponse(self.name)

class ListView(View):
    queryset = None
    template_name = None
    def get(self, request):
        return render(request, self.template_name, {"object_list": self.queryset})


class ArticleList(ListView):
    queryset = Article.objects.all()
    template_name = 'post_app/blog-entries.html'
