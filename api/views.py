from django.shortcuts import render
from rest_framework import generics, permissions
from currency.models import *
from . import serializers
from rest_framework import viewsets
from . import permissions as overrided_permissions
import re
import yfinance as yf
import datetime

class CurrencyList(generics.ListAPIView): # CurrencyList provides read-only access (via get) to a list of currencies
    queryset = Currency.objects.all()
    serializer_class = serializers.CurrencySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    

class CurrencyDetail(generics.RetrieveAPIView): # CurrencyDetail - to one currency
    queryset = Currency.objects.all()
    serializer_class = serializers.CurrencySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]



class ExchangeRateList(generics.ListAPIView): 
    queryset = ExchangeRate.objects.all()
    serializer_class = serializers.ExchangeRateSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    

class ExchangeRateDetail(generics.RetrieveAPIView): 
    queryset = ExchangeRate.objects.all()
    serializer_class = serializers.ExchangeRateSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        currency_1 = self.kwargs.get('currency_1').upper()
        currency_2 = self.kwargs.get('currency_2').upper()

        
        if not Currency.objects.filter(name__iexact = currency_1).exists(): currency_1 = Currency.objects.create(name = currency_1)
        else: currency_1 = Currency.objects.get(name = currency_1)

        if not Currency.objects.filter(name__iexact = currency_2).exists(): currency_2 = Currency.objects.create(name = currency_2)
        else: currency_2 = Currency.objects.get(name = currency_2)

        if re.search("^[A-Za-z]*$", self.kwargs.get('currency_1')) and re.search("^[A-Za-z]*$", self.kwargs.get('currency_2')):
            if ExchangeRate.objects.filter(currency1=currency_1, currency2=currency_2, date__year=datetime.date.today().year, date__month=datetime.date.today().month, date__day=datetime.date.today().day).exists():
                return ExchangeRate.objects.get(currency1=currency_1, currency2=currency_2, date__year=datetime.date.today().year, date__month=datetime.date.today().month, date__day=datetime.date.today().day)
            else:
                exchange_data = yf.download(f'{currency_1}{currency_2}=X', start=datetime.date.today()).to_dict()

                open = next(iter(exchange_data['Open'].items()))[1]
                high = next(iter(exchange_data['High'].items()))[1]
                low = next(iter(exchange_data['Low'].items()))[1]
                close = next(iter(exchange_data['Close'].items()))[1]
                adj_close = next(iter(exchange_data['Adj Close'].items()))[1]
                date = next(iter(exchange_data['Close'].items()))[0]


                exchange_rate = ExchangeRate.objects.create(
                    currency1 = currency_1, 
                    currency2 = currency_2,
                    open_cost = open,
                    high_cost = high,
                    low_cost = low,
                    close_cost = close,
                    adj_close_cost = adj_close,
                    date = date,
                )

                return exchange_rate