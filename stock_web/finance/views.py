from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import SymbolForm
import certifi
import json
from urllib.request import urlopen
import requests
from .financedata import getfinancedata

def balancesheet(request):
    return HttpResponse("This is for Balancesheet")


# Create your views here.
API_KEY = '6ea77b917e9ac025a7fab4f39229fdf1'
base_url =  'https://financialmodelingprep.com/api'

def incomestatement(request):
    if request.method == 'POST':
        form = SymbolForm(request.POST)
        if form.is_valid():
            symbol = request.POST['symbol']
            if 'ticker' in request.POST:
                base_url =  'https://financialmodelingprep.com/api'
                data_type = 'income-statement'
                url = f"{base_url}/v3/{data_type}/{symbol}?period=annual&apikey={API_KEY}"
                response = urlopen(url, cafile=certifi.where())
                data = response.read().decode("utf-8")
                arr = []
                arr = json.loads(data)
                context = {'d': arr, 'symbol': symbol}
                return render(request, 'financedata/incomestatement.html', context)
            else:
                return HttpResponse('Something is not working at 1')
        else:
            return HttpResponse('Something is not working at 2')
    else:
        form = SymbolForm()
    return render(request, 'financedata/incomestatement.html', {'form':form})
    

    # def financial_statements(request):
    # if request.method == 'POST':
    #     form = TickerForm(request.POST)
    #     if form.is_valid():
    #         ticker = request.POST['ticker']
    #         if 'symbol' in request.POST:
    #             base_url =  'https://financialmodelingprep.com/api'
    #             data_type = 'income-statement'
    #             url = f"{base_url}/v3/{data_type}/{ticker}?period=annual&apikey={API_KEY}"
    #             response = urlopen(url, cafile=certifi.where())
    #             data = response.read().decode("utf-8")
    #             arr = []
    #             arr = json.loads(data)
    #             context = {'d': arr, 'ticker': ticker}
    #             return render(request, 'financial_statement.html', context)
    #         else:
    #             return HttpResponse('Something is not working at 1')
    #     else:
    #         return HttpResponse('Something is not working at 2')
    # else:
    #     form = TickerForm()
    # return render(request, 'financial_statement.html', {'form':form})
       




            