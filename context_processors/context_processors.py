from post_app.models import *
from social.models import Social
from django.core.paginator import Paginator


def recent_article(request):
    recent_articles = Article.objects.order_by('updated_at')[:3]
    categories = Category.objects.all()
    return {'recent_articles': recent_articles, 'categories': categories}


def published_articles(request):
    published_article = Article.objects.published()
    paginator = Paginator(published_article, 2)
    object_list = paginator.get_page(request.GET.get('page'))
    return {'published_articles': object_list}

def published_article(request):
    published_article = Article.objects.published()
    return {'published_article': published_article}


def social_links(request):
    social_link = Social.objects.all()
    return {'social_links': social_link}
