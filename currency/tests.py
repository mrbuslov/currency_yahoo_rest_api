from django.test import TestCase

# import yfinance as yf

# # gold = yf.Ticker("EURUSD=X")
# forex_data = yf.download('EURUSD=X', start='2022-09-26')
# # print(type(forex_data))
# print(forex_data.to_dict())

# # print(gold.info['currency'])
# # print(gold.info['exchange'])



dic = {'Open': {'2022-09-26 00:00:00': 0.9692739844322205}}
print(iter(dic['Open']))


dict_pairs = dic['Open'].items()
pairs_iterator = iter(dict_pairs)
first_pair = next(pairs_iterator)
print(first_pair[1])