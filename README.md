# currency_yahoo_rest_api
Created Django Rest Api to find out about exchange rates through Yahoo

# Task
We’d like you to build a REST API for us - a basic currency exchange database
interacting with external API. Here’s full specification of endpoints that we’d like it to
have:

GET /currency/:
Should fetch a list of all currencies already present in the applicationdatabase.
Additional filtering, sorting is fully optional - but some implementation is abonus.
GET /currency/EUR/USD/:
Should return exchange rate for EUR/USD

Rules
Load data from external database. We recommend Yahoo and https://github.com/ranaroussi/yfinance but you can change.
Goal is to implement the REST API in Django. You're free to use any third-partylibraries - sharing your reasoning behind choosing them is welcome!
Database selection is limited to MySQL or SqlLite
Basic tests of endpoints are obligatory. Their exact scope is left up to you.
We do not require any authorization/authentication system(s).
The application's code should be in a public repository!

# Comments
1. Yahoo is a great stock price tracking tool. Its big difference from other simpler services is that it gives price indicators at the opening and closing of the market, as well as the final price of the currency. The rest of the services give one value.
