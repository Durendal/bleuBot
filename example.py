import bleuBot
import json

def main():
	# Replace these with your values from bleutrade.com
	key = "YOUR_API_KEY"
	secret = "YOUR_API_SECRET"

	# Lets take this baby for a spin!
	bleubot = bleuBot.bleuBot(key, secret)

	# Uncomment the following examples to test out some features

	# getBalance(coin)
	#btcbalance = bleubot.getBalance("BTC")
	#potbalance = bleubot.getBalance("POT")
	#ltcbalance = bleubot.getBalance("LTC")
	#print "Balances of BTC, POT, and LTC: "
	#print btcbalance
	#print potbalance
	#print ltcbalance

	# getMarketSummaries()
	#marketSummaries = bleubot.getMarketSummaries()
	#print "Market Summaries: "
	#print marketSummaries	
	#with open("marketSummaries.txt", "wb") as writeFile:
	#	json.dump(marketSummaries, writeFile)

	# getOrderBook(market, type, depth)
	#orderBook = bleubot.getOrderBook("TRL_HTML5", "ALL", 2)
	#with open("orderBook.txt", "wb") as writeFile:
	#	json.dump(orderBook, writeFile)
	

	# Donate to the developer :D, feel free to modify currency or value
	# transferToDurendal = bleubot.transfer("LTC", "1", "Durendal")
	# print transferToDurendal
	
if __name__ == '__main__':
	main()