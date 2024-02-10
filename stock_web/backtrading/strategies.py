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
import datetime as dt
import pandas as pd
import os
import pyfolio as pf
# from backtrading import strategies



class TestStrategy(bt.Strategy):
    lines = ('rsi',) #, to consider it as a list, else it will think as a string.
    params = (       
        ('rsi_period', 14),
        ('rsi_high', 70),
        ('rsi_low', 30)
    )
      
    # def log(self, txt, dt=None):
    #     dt = dt or self.datas[0].datetime.datetime(0)
    #     print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self, take_profit, stop_loss):
        self.take_profit = take_profit
        self.stop_loss = stop_loss
        
        self.dataclose = self.datas[0].close
        self.open = self.datas[0].open
        
        self.buyprice = None
        self.sellprice = None
        self.order = None

        #Indicators 
        self.rsi = bt.indicators.RSI_EMA(self.dataclose, period = self.params.rsi_period)

    
    def next(self):
        if self.order:
            return
        
        if not self.position:
            if self.rsi<self.params.rsi_low:
                self.order = self.buy()
               
        else:
            take_profit_price = self.buyprice * (1.0 + self.take_profit)
            stop_loss_price = self.buyprice * (1.0 - self.stop_loss)

            if (self.rsi>self.params.rsi_high) or (self.dataclose[0]>=take_profit_price) or (self.dataclose[0]<=stop_loss_price):
                self.order = self.sell()