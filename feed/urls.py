
# feed/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='feed/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('feed/', views.feed, name='feed'),
    path('tweet/', views.create_tweet, name='create_tweet'),
    path('register/', views.register, name='register'),
    path('friends/', views.friends_view, name='friends'),
    path('add_comment/', views.add_comment, name='add_comment'),
]

