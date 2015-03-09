import requests
import hmac
import hashlib
import time

class bleuBot:

	# Constructor
	def __init__(self, apikey = None, apisecret = None, nonce = False, baseurl = "https://bleutrade.com/api/v2/"):
		self._url = ""
		self._baseurl = baseurl
		self._params = {}
		self._apiKey = apikey
		self._apiSecret = apisecret
		self._nonce = nonce
		self._setBaseURL()


	# Setters
	def _setURL(self, url):
		self._url = url

	def _setParams(self, params):
		self._params = params

	# Getters
	def getURL(self):
		
		return self._url

	def getParams(self):
		
		return self._params

	def getAPIKey(self):
		
		return self._apiKey

	def getAPISecret(self):
		
		return self._apiSecret

	def getBaseURL(self):
		
		return self._baseurl

	# Requests (GET and POST)
	def _getRequest(self, headers = None):
		if headers != None:
			r = requests.get(self.getURL(), params = self.getParams(), headers = headers)
		else:
			r = requests.get(self.getURL(), params = self.getParams())
		return r.json()

	def _postRequest(self, headers = None):
		if headers != None:
			r = requests.post(self.getURL(), params = self.getParams(), headers = headers)
		else:
			r = requests.post(self.getURL(), params = self.getParams())
		return r.json()


	def _setBaseURL(self):
		self._setURL(self._baseurl)


	# BleuTrade functions adapted from beefviper @ http://forum.bleutrade.com/index.php/topic,213.0.html
	
	# 'public/getcurrencies': Get a list of all coins traded
	# params: null
	# return: JSON 
	def getCurrencies(self):
		query = "public/getcurrencies"
		params = {}
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result
	
	# 'public/getmarkets': Get the list of all pairs traded
	# params: null
	# return: JSON
	def getMarkets(self):
		query = "public/getmarkets"
		params = {}
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result

	# 'public/getticker': Used to get the current tick values for a market
	# params: market: string (ex: BLUE_BTC)
	# return: JSON
	def getTicker(self, market):
		query = "public/getticker"
		params = { "market" : market }
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result

	# 'public/getmarketsummaries': Used to get the last 24 hour summary of all active markets
	# params: null
	# return: JSON
	def getMarketSummaries(self):
		query = "public/getmarketsummaries"
		params = {}
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result

	# 'public/getmarketsummary': Used to get the last 24 hour summary of specific market
	# params: market: string (ex: BLUE_BTC)
	# return: JSON
	def getMarketSummary(self, market):
		query = "public/getmarketsummary"
		params = { "market" : market }
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result

	# 'public/getorderbook': Loads the book offers specific market.
	# params: market: string (ex: BLUE_BTC)
	#         type:   string (BUY|SELL|ALL)
	#         depth:  int    (optional, default is 20)
	# return: JSON
	def getOrderBook(self, market, rType = "ALL", depth = 20):
		query = "public/getorderbook"
		params = { 
					"market" : market,
					"type" : rType,
					"count" : depth
				}
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result

	# 'public/getmarkethistory': Obtains historical trades of a specific market
	# params: market: string (ex: BLUE_BTC)
	#         count : int    (optional, default: 20, max: 200)
	# return: JSON
	def getMarketHistory(self, market, count = 20):
		query = "public/getmarkethistory"
		params = {
					"market" : market,
					"count" : count
				 }
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result
	
	# 'public/getcandles': Obtains candles format historical trades of a specific market
	# params: market    : string (ex: BLUE_BTC)
	#         period    : string (1m, 2m, 3m, 4m, 5m, 6m, 10m, 12m, 15m, 20m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 12h, 1d) 
	#         count     : int    (default: 1000, max: 999999)
	#         lasthours: int    (default: 24, max: 720)
	# return: JSON
	def getCandles(self, market, period = "30m", count = 1000, lasthours = 24):
		query = "public/getcandles"
		params = {
					"market" : market,
					"period" : period,
					"count" : count,
					"lasthours" : lasthours
				 }
		self._setParams(params)
		result = self._makePublicAPICall(query)
		return result

	# 'market/buylimit': Use to send BUY orders
	# params: market  : string (ex: BLUE_BTC)
	#         rate    : string (ex: 1234.12345678)
	#         quantity: string (ex: 1234.12345678)
	#         comments: string (optional, up to 128 characters
	# return: JSON
	def buyLimit(self, market, rate, quantity, comments = ""):
		query = "market/buylimit"
		params = {
					"market" : market,
					"rate" : rate,
					"quantity" : quantity,
					"comments" : comments
				 }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'market/selllimit': Use to send SELL orders
	# params: market  : string (ex: BLUE_BTC)
	#         rate    : string (ex: 1234.12345678)
	#         quantity: string (ex: 1234.12345678)
	#         comments: string (optional, up to 128 characters)
	# return: JSON
	def sellLimit(self, market, rate, quantity, comments = ""):
		query = "market/selllimit"
		params = {
					"market" : market,
					"rate" : rate,
					"quantity" : quantity,
					"comments" : comments
				 }
		result = self.makePrivateCallAPI(query)
		return result

	# 'market/cancel': Use to cancel an order
	# params: orderid: int
	# return: JSON
	def cancel(self, orderid):
		query = "market/cancel"
		params = { "orderid" : orderid }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'market/getopenorders': Use to list your open orders
	# params: null
	# return: JSON
	def getOpenOrders(self):
		query = "market/getopenorders"
		params = {}
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'account/getbalances': Use to get the balance of all your coins
	# params: currencies: string (optional, default=ALL, eg: 'DOGE;BTC;LTC')
	# return: JSON
	def getBalances(self):
		query = "account/getbalances"
		params = {}
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'account/getbalance': Use to get the balance of a specific currency 
	# params: currency: string (ex: BTC)
	# return: JSON
	def getBalance(self, currency):
		query = "account/getbalance"
		params = { "currency" : currency }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'account/getdepositaddress': Use to get the deposit address of specific coin
	# params: currency: string (ex: BTC)
	# return: JSON
	def getDepositAddress(self, currency):
		query = "account/getdepositaddress"
		params = { "currency" : currency }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result
	
	# 'account/withdraw': Use to withdraw their currencies to another wallet
	# params: currency: string (ex: BTC)
	#         quantity: string (ex: 1234.12345678)
	#         address : string (ex: nOtReAl4kjh5kjhv98er76t938dsf)
	# return: JSON
	def withdraw(self, currency, quantity, address):
		query = "account/withdraw"
		params = {
					"currency" : currency,
					"quantity" : quantity,
					"address" : address
				 }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'account/transfer': Use to direct transfer their currencies to another user, without fees
	# params: currency : string (ex: BTC)
	#         quanitity: string (ex: 1234.122345678)
	#         touser   : string (username, supplied by the user, also seen in chat) 
	# return: JSON
	def transfer(self, currency, quantity, touser):
		query = "account/transfer"
		params = {
					"currency" : currency,
					"quantity" : quantity,
					"touser" : touser
				 }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'account/getorder': Use to get the data given order
	# params: orderid: int
	# return: JSON
	def getOrder(self, orderid):
		query = "account/getorder"
		params = { "orderid" : orderid }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# account/getorders - Use to list your orders
	# params: market
	# order_status: (ALL, OK, OPEN, CANCELED) 
	# return: JSON
	def getOrders(self, market, orderstatus):
		query = "account/getorders"
		params = { 
					"market" : market,
					"orderstatus" : orderstatus
				 }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# account/getorderhistory - Use for historical trades of a given order.
	# params: orderid
	# return: JSON
	def getOrderHistory(self, orderid):
		query = "account/getorderhistory"
		params = { "orderid" : orderid }
		self._setParams(params)
		result = self._makePrivateAPICall(query)
		return result

	# 'make_public_api_call': takes constructed query and calls public api
	# params: query
	# return: result
	def _makePublicAPICall(self, query):
		# Set _url to the base URL
		self._setBaseURL()

		# Update the URL to include query
		self._setURL(self.getURL() + query)
		
		result = self._getRequest()
		
		# Clear the parameter list
		emptyDict = {}
		self._setParams(emptyDict)
		
		return result

	# 'make_private_api_call': takes constructed query and calls private api
	# params: query
	# return: result
	def _makePrivateAPICall(self, query):
		# Verify that API Key and Secret are available
		if self._apiSecret == None or self._apiKey == None:
			print "You must set a valid API Key and API Secret to make private API Calls"
			return None

		# Set _url to the base URL
		self._setBaseURL()
		
		# Check if user has selected to use a nonce
		if self._nonce == True:
			self._params['nonce'] = string(int(time.time()))

		# Add API Key to parameter list
		self._params['apikey'] = self.getAPIKey()

		# Update the URL to include query
		self._setURL(self.getURL() + query)

		# Generate the apisign
		sign = hmac.new(self.getAPISecret(), self._formHashURL(), hashlib.sha512).hexdigest()
		
		# Add custom header
		headers = { "apisign" : sign }
		
		result = self._getRequest(headers)
		
		# Clear the parameter list
		emptyDict = {}
		self._setParams(emptyDict)

		return result		

	def _formHashURL(self):
		
		returnURL = self.getURL() + "?"
		# Generate a url with GET parameters in it, to be used in hashing the sign
		for key, value in self._params.iteritems():
			returnURL += key + "=" + value + "&"
		# Trim trailing &
		returnURL = returnURL[:-1]
		return returnURL
