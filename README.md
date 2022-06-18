Python-BtxPro(Dovewallet)
=

Python-Dovewallet is a Python library for the Dovewallet API v1.1.

Use this to sell mined coins, write 3 trading bots or do whatever your heart desires.


Getting started
=

Get your API keys from https://dovewallet.com/en/my-page/api, download dovewallet.py and place it in the same directory as your script.

    #!/usr/bin/env python
    from dovewallet import dovewallet
    
    api = dovewallet('key', 'secret')
    
    print api.getticker('BTC-DASH')


example.py
=

The example program buys 100 DOGE for the current price and sells them for a higher price. It also shows some other functions.  

Check out https://developer.dovewallet.com/api/v1/ or read the source code for a full list of functions.
