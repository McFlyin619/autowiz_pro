from django.contrib import admin
from django.urls import path, include
from .views import business_register, customer_register, user_login, user_logout

app_name = 'account'

urlpatterns = [
    path('sign-up/', customer_register, name='customer_register'),
    path('pro-sign-up/',business_register, name='business_register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
]
