from datetime import datetime
from locale import currency
from statistics import mode
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', unique=True)
    symbol = models.CharField(max_length=3, verbose_name='Symbol', blank=True)

    def __str__(self):
        return self.name
    
    # Changing our model for the admin panel
    class Meta:
        verbose_name_plural='Currencies'
        verbose_name= 'Currency'
        ordering=['name']


# We will create separate table for writing exchange rates for bigger productivity in terms of time (api request to yfinance is longer than db request)
class ExchangeRate(models.Model):
    currency1 = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, verbose_name='Currency 1', related_name='exchange_currency1')
    currency2 = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, verbose_name='Currency 2', related_name='exchange_currency2')
    open_cost = models.DecimalField(verbose_name='Open cost', decimal_places=10, max_digits=15) 
    high_cost = models.DecimalField(verbose_name='High cost', decimal_places=10, max_digits=15)  
    low_cost = models.DecimalField(verbose_name='Low cost', decimal_places=10, max_digits=15)
    close_cost = models.DecimalField(verbose_name='Close cost', decimal_places=10, max_digits=15)
    adj_close_cost = models.DecimalField(verbose_name='Adjusted close cost', decimal_places=10, max_digits=15)
    date = models.DateTimeField(verbose_name='Date', default=datetime.now())

    def __str__(self):
        return f'{self.currency1} to {self.currency2}'
    
    # Changing our model for the admin panel
    class Meta:
        verbose_name_plural='ExchangeRates'
        verbose_name= 'ExchangeRate'
        ordering=['currency1']
