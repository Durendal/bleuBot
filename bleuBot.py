import requests
import json
import hmac
import hashlib

class bleuBot:

	# Constructor
	def __init__(self, apikey, apisecret, baseurl = "https://bleutrade.com/api/v2/"):
		self._url = ""
		self._baseurl = baseurl
		self._params = {}
		self._apiKey = apikey
		self._apiSecret = apisecret
		self.setBaseURL()


	# Setters
	def setURL(self, url):
		self._url = url

	def setParams(self, params):
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
	def getRequest(self, headers=None):
		if headers != None:
			r = requests.get(self.getURL(), params = self.getParams(), headers = headers)
		else:
			r = requests.get(self.getURL(), params = self.getParams())
		return r.json()

	def postRequest(self):
		r = requests.post(self.getURL(), params = self.getParams())
		return r.json()


	def setBaseURL(self):
		self._url = self._baseurl


	# BleuTrade functions adapted from beefviper @ http://forum.bleutrade.com/index.php/topic,213.0.html
	def getCurrencies(self):
		query = "public/getcurrencies"
		params = {}
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def getMarkets(self):
		query = "public/getmarkets"
		params = {}
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def getTicker(self, market):
		query = "public/getticker"
		params = { "market" : market }
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def getMarketSummaries(self):
		query = "public/getmarketsummaries"
		params = {}
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def getMarketSummary(self, market):
		query = "public/getmarketsummary"
		params = { "market" : market }
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def getOrderBook(self, market, rType = "ALL", depth = 20):
		query = "public/getorderbook"
		params = { 
					"market" : market,
					"type" : rType,
					"count" : depth
				}
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def getMarketHistory(self, market, count = 20):
		query = "public/getmarkethistory"
		params = {
					"market" : market,
					"count" : count
				 }
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result
		
	def getCandles(self, market, period = "30m", count = 1000, lasthours = 24):
		query = "public/getcandles"
		params = {
					"market" : market,
					"period" : period,
					"count" : count,
					"lasthours" : lasthours
				 }
		self.setParams(params)
		result = self.makePublicAPICall(query)
		return result

	def buyLimit(self, market, rate, quantity, comments = ""):
		query = "market/buylimit"
		params = {
					"market" : market,
					"rate" : rate,
					"quantity" : quantity,
					"comments" : comments
				 }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

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

	def cancel(self, orderid):
		query = "market/cancel"
		params = { "orderid" : orderid }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getOpenOrders(self):
		query = "market/getopenorders"
		params = {}
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getBalances(self):
		query = "account/getbalances"
		params = {}
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getBalance(self, currency):
		query = "account/getbalance"
		params = { "currency" : currency }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getDepositAddress(self, currency):
		query = "account/getdepositaddress"
		params = { "currency" : currency }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def withdraw(self, currency, quantity, address):
		query = "account/withdraw"
		params = {
					"currency" : currency,
					"quantity" : quantity,
					"address" : address
				 }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def transfer(self, currency, quantity, touser):
		query = "account/transfer"
		params = {
					"currency" : currency,
					"quantity" : quantity,
					"touser" : touser
				 }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getOrder(self, orderid):
		query = "account/getorder"
		params = { "orderid" : orderid }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getOrders(self, market, orderstatus):
		query = "account/getorders"
		params = { 
					"market" : market,
					"orderstatus" : orderstatus
				 }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def getOrderHistory(self, orderid):
		query = "account/getorderhistory"
		params = { "orderid" : orderid }
		self.setParams(params)
		result = self.makePrivateAPICall(query)
		return result

	def makePublicAPICall(self, query):
		self.setBaseURL()
		self.setURL(self.getURL() + query)
		result = self.getRequest()
		emptyDict = {}
		self.setParams(emptyDict)
		return result

	def makePrivateAPICall(self, query):
		self.setBaseURL()
		self._params['apikey'] = self.getAPIKey()
		self.setURL(self.getURL() + query)
		sign = hmac.new(self.getAPISecret(), self.formHashURL(), hashlib.sha512).hexdigest()
		headers = { "apisign" : sign }
		result = self.getRequest(headers)
		emptyDict = {}
		self.setParams(emptyDict)
		return result		

	def formHashURL(self):
		
		returnURL = self.getURL() + "?"
		for key, value in self._params.iteritems():
			returnURL += key + "=" + value + "&"
		returnURL = returnURL[:-1]
		return returnURL
