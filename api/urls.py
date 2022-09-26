from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('currency/', views.CurrencyList.as_view()),
    path('currency/<int:pk>/', views.CurrencyDetail.as_view()),
    path('exchange_rate/', views.ExchangeRateList.as_view()),
    path('currency/<str:currency_1>/<str:currency_2>/', views.ExchangeRateDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)