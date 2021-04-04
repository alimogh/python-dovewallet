#!/usr/bin/env python
# This program buys some Dgbcoins and sells them for a bigger price
from dovewallet import dovewallet

# Get these from https://dovewallet.com/en/my-page/api
api = dovewallet('key', 'secret')

# Market to trade at
fee = 0.001
trade = 'ETH'
currency = 'DGB'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 10
# How big of a profit you want to make
your_profit = 1.03 
multiplier = your_profit + (2*fee)

# Getting the ETH price for DGB
dgbsummary = api.getmarketsummary(market)
dgbprice_last = dgbsummary[0]['Last']
print 'The price for {0} is {1:.8f} {2}.'.format(currency, dgbprice_last, trade)

# Buying 10 DGB for ETH
dgbprice_buy = ( dgbprice * 0.995 )
print 'Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, dgbprice_buy, trade)
api.buylimit(market, amount, dgbprice_buy)

# Multiplying the price by the multiplier
dgbprice_sell = round(dgbprice_buy*multiplier, 8)

# Selling 9.98 DGB for the  new price
print 'Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, dgbprice_sell, trade)
api.selllimit(market, amount, dgbprice_sell)

# Gets the DGB balance
dgbbalance = api.getbalance(currency)
print "Your balance is {0} {1}.".format(dgbbalance['Available'], currency)

# For a full list of functions, check out dovewallet.py or https://developer.dovewallet.com/api/v1/
# 2021/04/04
