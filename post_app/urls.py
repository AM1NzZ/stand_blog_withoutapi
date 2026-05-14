from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:title>', views.post_detail, name='post_detail'),
    path('category/<str:category>', views.sort_article_by_category, name='sort_by_category'),
]