from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('incomestatement/', views.incomestatement, name='incomestatement'),
    path('balancesheet/', views.balancesheet, name = 'bss'),
]