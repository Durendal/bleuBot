import bleuBot

def main():
	key = "YOUR_KEY_HERE"
	secret = "YOUR_SECRET_HERE"
	bleubot = bleuBot.bleuBot(key, secret)
	btcbalance = bleubot.getBalance("BTC")
	potbalance = bleubot.getBalance("POT")
	ltcbalance = bleubot.getBalance("LTC")
	print btcbalance
	
	print potbalance
	
	print ltcbalance
	

if __name__ == '__main__':
	main()