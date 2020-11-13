from django.contrib import admin
from django.urls import path , include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup', views.handlesignup, name='handlesignup'),
]