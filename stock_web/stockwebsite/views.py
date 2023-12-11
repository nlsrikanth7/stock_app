from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from yahoo_fin.stock_info import *
import yfinance as yf
import datetime as dt
from . import middlewares
import requests
import json
import pandas as pd 
import numpy as np
from .forms import getstockdatamodelform, TickerForm
from fredapi import Fred
# from .addpricedata import getpricedata

fred_key = '975e2fa0a5fc6a9208096237b1411b64'
fred = Fred(api_key=fred_key)

def homepage(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            if 'symbol' in request.POST:
                start = dt.datetime(2023,1,1)
                end = dt.datetime.now()
                df = yf.download(ticker, start, end)
                df = df.to_csv(f'Data/{ticker}.csv')
                data = pd.read_csv(f'Data/{ticker}.csv')
                json_records = data.reset_index().to_json(orient='records')
                arr = []
                arr = json.loads(json_records)
                context = {'d': arr}
                return render(request, 'index.html', context)
            else:
                return HttpResponse('Something is not working at 1')
        else:
            return HttpResponse('Something is not working at 2')
    else:
        form = TickerForm()
    return render(request, 'index.html', {'form':form})
    

def GDP(request):
    start = dt.datetime(2010,1,1)
    end = dt.datetime.now()
    df = fred.get_series('GDP', observation_start=start, observation_end= end)
    df = df.reset_index()
    df = df.to_csv(f"Data/GDP.csv", header=['Date', 'GDPValue'])
    data = pd.read_csv(f'Data/GDP.csv')
    json_records = data.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_records)
    gdp = {'gdp': arr}
    return render(request, 'gdp.html', gdp)

def CPI(request):
    start = dt.datetime(2010,1,1)
    end = dt.datetime.now()
    df = fred.get_series('USACPALTT01CTGYM',observation_start=start, observation_end=end)
    df = df.reset_index()
    df = df.to_csv(f"Data/CPI.csv", header=['Date', 'CPI_Index'])
    data = pd.read_csv(f'Data/CPI.csv')
    json_records = data.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_records)
    cpi = {'cpi': arr}
    return render(request, 'cpi.html', cpi)

def PPI(request):
    start = dt.datetime(2010,1,1)
    end = dt.datetime.now()
    df = fred.get_series('PPIACO',observation_start=start, observation_end=end)
    df = df.reset_index()
    df = df.to_csv(f"Data/PPI.csv", header=['Date', 'PPI_Index'])
    data = pd.read_csv(f'Data/PPI.csv')
    json_records = data.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_records)
    ppi = {'ppi': arr}
    return render(request, 'ppi.html', ppi)




# DATABASE_ACCESS = True 
 # if request.method == 'POST':
    #     form = TickerForm(request.POST)
    #     if form.is_valid():
            
    #     return homepage(request)




