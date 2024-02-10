from django import forms
# import datetime as dt
# import pandas as pd

# end= dt.datetime.now()
# end_date = pd.to_datetime(end)
# start_date = pd.to_datetime(end_date) - pd.DateOffset(365*1)

class BacktestingForm(forms.Form):
    ticker = forms.CharField(label='Enter a Ticker Symbol')
    Starting_Portfolio_Value = forms.FloatField(label='Enter Starting Portfolio Value')
    backteststartdate = forms.DateField(
        
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': "date"
            }
        )
      )
    backtestenddate = forms.DateField(
         
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': "date"
            }
        )
      )
    


        