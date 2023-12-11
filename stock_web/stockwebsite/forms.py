from django import forms
from stockwebsite.models import Stockpricedata

class TickerForm(forms.Form):
    ticker = forms.CharField(label='Enter a Ticker Symbol', max_length=6)


class getstockdatamodelform(forms.ModelForm):
    class Meta:
        model = Stockpricedata
        fields = "__all__"
        