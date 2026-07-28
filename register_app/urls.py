from django.urls import path
from . import views
urlpatterns = [
    path('',views.register_user,name='registerUser'),
    path('profile/', views.user_profile, name='user_profile'),
]