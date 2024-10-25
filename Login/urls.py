from django.contrib import admin 
from django.urls import path, include
from .views import Login

login = Login.as_view({'post': 'login'})

urlpatterns = [
    path('login/', login), 
]