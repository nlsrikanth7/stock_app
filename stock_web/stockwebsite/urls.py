from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('GDP/', views.GDP, name='GDP'),
    path('CPI/', views.CPI, name='CPI'),
    path('PPI/', views.PPI, name='PPI'),
    # path('symbol/<str:pk>', views.getstocksymbol, name ='symbol'),
    # path('data/', views.getstockdata, name = 'getstockdata'),
    # path('display/', views.displaystockdata, name = 'displaystockdata'),
    # path('todb/', views.getdatatodb)
]