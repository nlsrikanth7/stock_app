import pandas as pd
import yfinance as yf
from django.core.management.base import BaseCommand
from stockwebsite.models import Stockpricedata

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello World")

