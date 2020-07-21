
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('calc', views.calc, name="calc"),
    path('calc1', views.calc1, name="calc1"),
    path('pos', views.pos, name="pos"),
    
]
