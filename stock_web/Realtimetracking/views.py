from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.http import HttpResponse
import time
import queue
from threading import Thread
import yfinance as yf


wiki = 'http://en.wikipedia.org/wiki/'
# Create your views here.
def stockPicker(request):
    
    # stock_picker = pd.read_html(wiki+'Dow_Jones_Industrial_Average')[1].Symbol.to_list()
    stock_picker = tickers_nasdaq()
    # stock_picker = tickers_sp500() # This API is not working
    # stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, 'realtimedata/stockpicker.html', {'stockpicker': stock_picker})

def stockTracker(request):
    stockpicker = request.GET.getlist('stockpicker')  # taking the list from above using GET.getlist method
   
    print(stockpicker)
    data = {}
    available_stocks = tickers_nasdaq()
    for stock in stockpicker:
        if stock in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    
    for stock in stockpicker:
        try:
            start = '2024-01-01'
            data= yf.download(f'{stock}')
            # data.append(yf.download(stock, start=start).reset_index())
            # data.to_csv(f'Data/{stock}.csv')
        except Exception as e:
            print(f'{stock} ==> {e}')    
    
    print(data)
    return render(request, 'realtimedata/stocktracker.html', {'data': data})

    # n_threads = len(stockpicker)
    # thread_list = []
    # que = queue.Queue()
    # start = time.time()
    # for i in stockpicker:
    #     result = get_quote_table(i)
    #     data.update({i: result})
    # for i in range(n_threads):
    #     thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args = (que, stockpicker[i]))
    #     thread_list.append(thread)
    #     thread_list[i].start()

    # for thread in thread_list:
    #     thread.join()

    # while not que.empty():
    #     result = que.get()
    #     data.update(result)
    # end = time.time()
    # time_taken =  end - start
    # print(time_taken)
            
    
  


    # data = {} # make a dict to render to front end

    # # we want code to pick only those stocks choosen by user 
    # # available_stocks = pd.read_html(wiki+'Dow_Jones_Industrial_Average')[1].Symbol.to_list()
    # available_stocks = tickers_nasdaq()
    
    # for i in stockspicker:
    #     if i in available_stocks:
    #         pass
    #     else:
    #         return HttpResponse ("Error")
    
    # # Threading
    # n_threads= len(stockspicker)
    # thread_list = []
    # que = queue.Queue()
    # start = time.time()  # we are using time module to compute processing time 
    # # for i in stockspicked:
    # #     details = get_quote_table(i)
    # #     data.update({i: details})
    # for i in range(n_threads):
    #     thread = Thread(target=lambda q, arg1: q.put({stockspicker[i]: get_quote_table(arg1)}), args=(que, stockspicker[i]))
    #     thread_list.append(thread)
    #     thread_list[i].start()

    # for thread in thread_list:
    #     thread.join()

    # while not que.empty():
    #     result = que.get()
    #     data.update(result)        
    # end=time.time()
    # time_taken = end-start
    # print(time_taken)

    # print(data)
    # return render(request, 'realtimedata/stocktracker.html', {'data': data})