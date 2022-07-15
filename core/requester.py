import requests
import time

def requester(url):
	time.sleep(10) # https://www.blockchain.com/api/q
	return requests.get('https://blockchain.info/rawaddr/' + url).text
