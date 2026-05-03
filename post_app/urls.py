from django.urls import path
from . import views
urlpatterns = [
    path('<str:title>', views.post_detail, name='post_detail'),
]