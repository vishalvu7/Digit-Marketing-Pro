from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('home',views.home,name="home"),
    path('whatsappcredit',views.whatsappcredit,name="whatsappcredit"),
    path('iframe',views.my_iframe_view,name="iframe"),
    path('logout', views.logout_user, name='logout'),
    path('passwordreset', views.passwordreset, name='passwordreset')
    
    
]

