import requests

def requester(url):
	sleep 10 # limited to one request per 10 seconds alas https://www.blockchain.com/api/q
	return requests.get('https://blockchain.info/rawaddr/' + url).text
