from unicodedata import category

from post_app.models import *

def recent_article(request):
    recent_articles = Article.objects.order_by('updated_at')[:3]
    categories = Category.objects.all()
    return {'recent_articles': recent_articles , 'categories':categories}