from django import forms

class SymbolForm(forms.Form):
    symbol = forms.CharField(label = 'Enter the Symbol', max_length=6)