from __future__ import (absolute_import, division, print_function,unicode_literals)
from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from .forms import SymbolForm
import certifi
import json
from urllib.request import urlopen
import requests
import numpy as np
from datetime import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import backtrader as bt
import yfinance as yf
import datetime
import pandas as pd
import os
import pyfolio as pf
# from backtrading import strategies
from backtrading.strategies import TestStrategy
from stockwebsite.forms import TickerForm
from .forms import BacktestingForm


TAKE_PROFIT = 0.2
STOP_LOSS = 0.05

def index(request):
    return render(request, "index.html", {})

def backtrading(request):
    if request.method == 'POST':
        # form = TickerForm(request.POST) 
        form = BacktestingForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            Starting_Portfolio_Value = request.POST['Starting_Portfolio_Value']
            backteststartdate = request.POST['backteststartdate']
            backtestenddate = request.POST['backtestenddate']
            start = pd.to_datetime(backteststartdate)
            end= pd.to_datetime(backtestenddate)
            df = yf.download(ticker, start, end)
            df = df.to_csv(f'Data/{ticker}.csv')
            # data_folder = '/Users/shrikanthnallapati/Projects/stock_app/Data'
            data = pd.read_csv(f'Data/{ticker}.csv') 
            data['Date'] = pd.to_datetime(data['Date'],utc=True)
            data=data.set_index('Date')
            data = data.drop('Adj Close', axis=1)
            if 'rsi' in request.POST:
                cerebro = bt.Cerebro()
                cerebro.broker.setcash(int(Starting_Portfolio_Value))
                data = bt.feeds.PandasData(dataname=data,datetime=None, open=0, high=1, low=2, close=3, volume =4, openinterest = -1) # -1 if not there, and 0,1,2,3,4 represents the columns 

                cerebro.adddata(data)
                cerebro.addstrategy(TestStrategy, take_profit=TAKE_PROFIT, stop_loss=STOP_LOSS)
                # strats = cerebro.optstrategy(TestStrategy,rsi_period=range(10, 31))
                cerebro.addsizer(bt.sizers.PercentSizer, percents = 99)
                # cerebro.addsizer(bt.sizers.FixedSize, stake = 25)
                cerebro.broker.setcommission(commission=0.0001)
                cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name ='myanalysis')
                Starting_Portfolio_Value = cerebro.broker.getvalue()
                cerebro.run()
                # thestrats = cerebro.run()
                # thestrat = thestrats[0]
                Final_Portfolio_Value = cerebro.broker.getvalue()
                profit = (Final_Portfolio_Value-Starting_Portfolio_Value)
                result= {'Starting_value':Starting_Portfolio_Value,'Ending_value': Final_Portfolio_Value, 'Profit': profit}
                return render(request, 'backtest/rsi.html', result)
            else:
                return HttpResponse('Something is not working at 1')
        else:
            return HttpResponse('Something is not working at 2')
    else:
        form = BacktestingForm()
    return render(request, 'backtest/rsi.html', {'form':form})



# def stockvisualizer(request):
#     if request.method == 'POST':
#         form = TickerForm(request.POST)
#         if form.is_valid():
#             ticker = request.POST['ticker']
#             start = dt.datetime(2023,1,1)
#             end = dt.datetime.now()
#             df = yf.download(ticker, start, end)
#             df = df.to_csv(f'Data/{ticker}.csv')
#             if 'symbol' in request.POST:
#                 # start = dt.datetime(2023,1,1)
#                 # end = dt.datetime.now()
#                 # df = yf.download(ticker, start, end)
#                 # df = df.to_csv(f'Data/{ticker}.csv')
#                 data = pd.read_csv(f'Data/{ticker}.csv')  
#                 # data.to_sql(Stockpricedata, con=engine, if_exists='replace')  
#                 # return HttpResponse('Data added to DB')
#                 json_records = data.reset_index().to_json(orient='records')
#                 arr = []
#                 arr = json.loads(json_records)
#                 context = {'ticker':ticker,'d': arr}
#                 return render(request, 'stockdata/stockvisualizer.html', context)
#             elif 'rsi' in request.Projects:
#                 data = pd.read_csv(f'Data/{ticker}.csv') 
#                 data['Date'] = pd.to_datetime(data['Date'],utc=True)
#                 data=data.set_index('Date')
#                 data = data.drop('Adj Close', axis=1)
#                 cerebro = bt.Cerebro()
#                 cerebro.broker.setcash(15000.0)
#                 data = bt.feeds.PandasData(dataname=data,datetime=None, open=0, high=1, low=2, close=3, volume =4, openinterest = -1) # -1 if not there, and 0,1,2,3,4 represents the columns 
#                 cerebro.adddata(data)
#                 cerebro.addstrategy(TestStrategy, take_profit=TAKE_PROFIT, stop_loss=STOP_LOSS)
#                 # strats = cerebro.optstrategy(TestStrategy,rsi_period=range(10, 31))
#                 cerebro.addsizer(bt.sizers.PercentSizer, percents = 99)
#                 # cerebro.addsizer(bt.sizers.FixedSize, stake = 25)
#                 cerebro.broker.setcommission(commission=0.0001)
#                 cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name ='myanalysis')
#                 Starting_Portfolio_Value: cerebro.broker.getvalue()
#                 thestrats = cerebro.run()
#                 thestrat = thestrats[0]
#                 Final_Portfolio_Value: cerebro.broker.getvalue()
#                 profit = (Final_Portfolio_Value-Starting_Portfolio_Value)
#                 result= {'Starting_value':Starting_Portfolio_Value,'Ending_value': Final_Portfolio_Value, 'Profit': profit}
#                 return render(request, 'backtest/rsi.html', result)
#         else:
#             return HttpResponse('Something is not working at 2')
#     else:
#         form = TickerForm()
#     return render(request, 'stockdata/stockvisualizer.html', {'form':form})
