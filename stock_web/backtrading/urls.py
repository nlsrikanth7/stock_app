from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('rsi/', views.backtrading, name='rsi'),
    path('macd/', views.backtrading, name = 'macd'),
]