#!/usr/bin/env python
# This program buys some Dgbcoins and sells them for a bigger price
from dovewallet import dovewallet

# Get these from https://dovewallet.com/en/my-page/api
api = dovewallet('key', 'secret')

# Market to trade at
trade = 'ETH'
currency = 'DGB'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 50
# How big of a profit you want to make
multiplier = 1.1

# Getting the ETH price for DGB
dgbsummary = api.getmarketsummary(market)
dgbprice = dgbsummary[0]['Last']*0.995
print 'The price for {0} is {1:.8f} {2}.'.format(currency, dgbprice, trade)

# Buying 50 DGB for ETH
print 'Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, dgbprice, trade)
api.buylimit(market, amount, dgbprice)

# Multiplying the price by the multiplier
dgbprice = round(dgbprice*multiplier, 8)

# Selling 50 DGB for the  new price
print 'Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, dgbprice, trade)
api.selllimit(market, amount, dgbprice)

# Gets the DGB balance
dgbbalance = api.getbalance(currency)
print "Your balance is {0} {1}.".format(dgbbalance['Available'], currency)

# For a full list of functions, check out dovewallet.py or https://developer.dovewallet.com/api/v1/
# 2021/04/04
