from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    # API to post a comments
    path('postComment', views.postComment, name= 'postComment'),
    path('', views.bloghome, name='bloghome'),
    path('category/<str:cats>/', views.Category, name='category'),
    path('<str:slug>', views.blogpost, name='blogPost'),
    
]