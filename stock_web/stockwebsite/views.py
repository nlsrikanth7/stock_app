from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from yahoo_fin.stock_info import *
import sqlalchemy
from sqlalchemy import create_engine
from django.conf import settings
import yfinance as yf
import datetime as dt
# from . import middlewares
import json
import pandas as pd 
import numpy as np
from .forms import getstockdatamodelform, TickerForm
from fredapi import Fred
# from .addpricedata import getpricedata
import requests
from .models import Stockpricedata
from django_pandas.io import read_frame
import csv
from urllib.request import urlopen
import certifi


fred_key = '975e2fa0a5fc6a9208096237b1411b64'
fred = Fred(api_key=fred_key)

def index(request):
    return render(request, "index.html", {})

def contact(request):
    return render(request,'contact.html', {})

# Method # 3 (not working need to investigate)
# def stockvisualizer(request):
#     context = {}
#     if request.method == 'POST':
#         form = TickerForm(request.POST)
#         if form.is_valid():
#             tickerr = request.POST['ticker']
#             if 'symbol' in request.POST:
#                 start = dt.datetime(2023,1,1)
#                 end = dt.datetime.now()
#                 tickerr = tickerr.upper()
                # df = yf.download(ticker, start, end)
                # df['ticker']=ticker
                # df = df.to_csv(f'Data/{ticker}.csv')
                # data = pd.read_csv(f'Data/{ticker}.csv') 
                # # for index, row in data.iterrows():
                # Stockpricedata.objects.bulk_create([
                #         Stockpricedata(
                #             Date = row['Date'],
                #             Open = row['Open'],
                #             High = row['High'],
                #             Low = row['Low'],
                #             Close = row['Close'],
                #             AdjustedClose = row['Adj Close'],
                #             Volume = row['Volume'],
                #             ticker = row['ticker'] 
                #         ) for _, row in data.iterrows()
                #     ])
    #             datafromdb = Stockpricedata.objects.filter(ticker = "tickerr"),
                
    #             context = {'d': datafromdb, 'ticker': tickerr}
    #             return render(request, 'stockvisualizer.html', {'context':context})
    #         else:
    #             return HttpResponse('Something is not working at 1')
    #     else:
    #         return HttpResponse('Something is not working at 2')
    # else:
    #     form = TickerForm()
    # return render(request, 'stockvisualizer.html', {'form':form})


# Method # 2 (not working need to investigate)
# DATABASE_ACCESS = True 
# database_url = 'mysql://root:Shrikanth_1@localhost:3306/StockWebApplication'
# engine = sqlalchemy.create_engine('mysql://root:Shrikanth_1@localhost:3306/')
# engine = sqlalchemy.create_engine(database_url, echo=False)

# def stockvisualizer(request):
#     if request.method == 'POST':
#         form = TickerForm(request.POST)
#         if form.is_valid():
#             ticker = request.POST['ticker']
#             if 'symbol' in request.POST:
#                 start = dt.datetime(2023,1,1)
#                 end = dt.datetime.now()
#                 df = yf.download(ticker, start, end)
#                 stock_detail = json.loads(json.dumps(df))
#                 # df = df.to_csv(f'Data/{ticker}.csv')
#                 # data = pd.read_csv(f'Data/{ticker}.csv')  
#                 engine = sqlalchemy.create_engine('mysql://root:Shrikanth_1@localhost:3306/')
#                 stock_detail.to_sql(Stockpricedata._meta.db_table,engine, if_exists='replace', index=True, index_label='id')  
#                 # return HttpResponse('Data added to DB')
#                 return render(request, "index.html", {})
#             else:
#                 return HttpResponse('Something is not working at 1')
#         else:
#             return HttpResponse('Something is not working at 2')
#     else:
#         form = TickerForm()
#     return render(request, 'stockvisualizer.html', {'form':form})
    
# Method # 1 (Working, but not connected to Database)
def stockvisualizer(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            start = dt.datetime(2023,1,1)
            end = dt.datetime.now()
            df = yf.download(ticker, start, end)
            df = df.to_csv(f'Data/{ticker}.csv')
            if 'symbol' in request.POST:
                # start = dt.datetime(2023,1,1)
                # end = dt.datetime.now()
                # df = yf.download(ticker, start, end)
                # df = df.to_csv(f'Data/{ticker}.csv')
                data = pd.read_csv(f'Data/{ticker}.csv')  
                # data.to_sql(Stockpricedata, con=engine, if_exists='replace')  
                # return HttpResponse('Data added to DB')
                json_records = data.reset_index().to_json(orient='records')
                arr = []
                arr = json.loads(json_records)
                context = {'ticker':ticker,'d': arr}
                return render(request, 'stockdata/stockvisualizer.html', context)
            else:
                return HttpResponse('Something is not working at 1')
        else:
            return HttpResponse('Something is not working at 2')
    else:
        form = TickerForm()
    return render(request, 'stockdata/stockvisualizer.html', {'form':form})


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
    return render(request, 'economicdata/cpi.html', gdp)

def CPI(request):
    start = dt.datetime(2010,1,1)
    end = dt.datetime.now()
    # CPI - USACPALTT01CTGYM
    df1 = fred.get_series('MEDCPIM158SFRBCLE',observation_start=start, observation_end=end)
    df1 = df1.reset_index()
    df1 = df1.to_csv(f"Data/CPI.csv", header=['Date', 'CPI_Index'])
    cpidata = pd.read_csv(f'Data/CPI.csv')
    cpi_json_records = cpidata.reset_index().to_json(orient='records')
    cpi_arr = []
    cpi_arr = json.loads(cpi_json_records)
    
    #PPI
    df2 = fred.get_series('PPIACO',observation_start=start, observation_end=end)
    df2 = df2.reset_index()
    df2 = df2.to_csv(f"Data/PPI.csv", header=['Date', 'PPI_Index'])
    ppi_data = pd.read_csv(f'Data/PPI.csv')
    ppi_json_records = ppi_data.reset_index().to_json(orient='records')
    ppi_arr = []
    ppi_arr = json.loads(ppi_json_records)

    #GDP
    df = fred.get_series('GDP', observation_start=start, observation_end= end)
    df = df.reset_index()
    df = df.to_csv(f"Data/GDP.csv", header=['Date', 'GDPValue'])
    data = pd.read_csv(f'Data/GDP.csv')
    json_records = data.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_records)

    context = {'cpi': cpi_arr, 'gdp': arr, 'ppi': ppi_arr}
    return render(request, 'economicdata/cpi.html', context)

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
    return render(request, 'economicdata/cpi.html', ppi)

API_KEY = '6ea77b917e9ac025a7fab4f39229fdf1'







