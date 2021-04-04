 
#!/usr/bin/env python
# This program buys some Dash coins and sells them for a bigger price
from dovewallet import dovewallet

# Get these from https://dovewallet.com/en/my-page/api
api = dovewallet('key', 'secret')

# fee for trade
fee = 0.001
# Market to trade at
trade = 'ETH'
currency = 'DASH'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 0.005

# How big of a profit you want to make
your_profit = 1.03 
# (2*fee) = feeBuy + feeSell
multiplier = your_profit + (2*fee)

# Getting the ETH price for DASH
currencysummary = api.getmarketsummary(market)
price_last = currencysummary[0]['Last']
print 'The price for {0} is {1:.9f} {2}.'.format(currency, price_last, trade)

# Buying 0.005 DASH for ETH
price_buy = ( price_last * 0.995 )
print 'Buying {0} {1} for {2:.9f} {3}.'.format(amount, currency, price_buy, trade)
api.buylimit(market, amount*(1+fee) , price_buy)

# Multiplying the price by the multiplier
price_sell = round( price_buy * multiplier, 9)

# Selling 0.005 DASH for the  new price
print 'Selling {0} {1} for {2:.9f} {3}.'.format(amount, currency, price_sell, trade)
api.selllimit(market, amount, price_sell)

# Gets the DASH balance
balance = api.getbalance(currency)
print "Your balance is {0} {1}.".format(balance['Available'], currency)

# For a full list of functions, check out dovewallet.py or https://developer.dovewallet.com/api/v1/
# 2021/04/04
