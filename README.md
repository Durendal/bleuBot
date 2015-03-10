# bleuBot
A python bot for interacting with the BleuTrade API
bleuBot was written for Python 2.7 and has not been tested with 3.x
Donations are appreciated :)

	BTC: 1GicRCkw8EigtNdFwfTR6cFxM7uA8nNwbd
	LTC: LMzNLYqu1AKyvdwbdHjNZgkjAALKFJvpMB

=============
Dependencies:
=============
requests - http://docs.python-requests.org/en/latest/

======
About:
======
bleuBot is based on the php functions written by beefviper available at http://forum.bleutrade.com/index.php/topic,213.0.html

I have simply converted the code to python and placed it inside of a class to make working with things a little easier.

===========
Other Info:
===========
https://bleutrade.com/help/API - official API Documentation

=================
Member Functions:
=================

	_setURL(url)
		sets the URL for the next request

	_setParams(params)
		sets the parameters for the request(used in GET and POST requests)

	getURL()
		returns the currently set URL

	getParams()
		returns the currently set parameter list

	getAPIKey()
		returns the API Key set for that instance of the bot

	getAPISecret()
		returns the API Secret set for that instance of the bot

	getBaseURL()
		returns the base URL for bleutrade API requests: https://bleutrade.com/api/v2/

	_getRequest(headers = None)
		performs a GET based HTTP request and returns the result in json format

	_postRequest(headers = None)
		performs a POST based HTTP request and returns the result in json format

	_setBaseURL()
		sets _url to _baseurl

	getCurrencies()
		returns a list of all coins traded in json format

	getMarkets()
		returns a list of all pairs traded in json format

	getTicker(market)
		returns the current tick values for a market in json format

	getMarketSummaries()
		returns the last 24 hour summary of all markets in json format

	getMarketSummary(market)
		returns the last 24 hour summary of market in json format

	getOrderBook(market, type = 'ALL', depth = 20)
		returns the book offers of a specific market in json format

	getMarketHistory(market, count = 20)
		returns historical trades of a specific market in json format

	getCandles(market, period = '30m', count = 1000, lasthours = 24)
		returns candles format historical trades of a specific market

	buyLimit(market, rate, quantity, comments = '')
		Will send a buy order

	sellLimit(market, rate, quantity, comments = '')
		Will send a sell order

	cancel(orderID)
		Will cancel an order

	getOpenOrders()
		returns a list of open orders in json format

	getBalances()
		returns a list of balances for all coins in json format

	getBalance(currency)
		returns the balance of currency in json format

	getDepositAddress(currency)
		returns the deposit address of a specific coin in json format

	withdraw(currency, quantity, address)
		Will withdraw currencies to another wallet

	transfer(currency, quantity, touser)
		Will transfer quantity, of currency, to touser. Without fees.

	getOrder(orderid)
		returns the data for a given order in json format

	getOrders(market, orderstatus)
		returns a list of your orders in a given market, that correspond to the specified order status. in json format.

	getOrderHistory(orderid)
		returns data of historical trades in a given order in json format

	_makePublicAPICall(query)
		handles making the actual API request, used for public requests. 

	_makePrivateAPICall(query)
		handles making the actual API request, used for private requests. 

	_formHashURL()
		generates the URL needed to make the apisign header

=================
Member Variables:
=================

	_url - the URL used for the next HTTP Request
	_baseurl - the base url of the bleu trade API: https://bleutrade.com/api/v2/
	_params - a dictionary of parameters for each request
	_apiKey - the API Key for your bleutrade user account
	_apiSecret - the API Secret for your bleutrade user account
	_nonce - Values: True or False, indicates whether or not to use a nonce on private API calls