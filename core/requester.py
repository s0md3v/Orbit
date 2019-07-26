import requests

def requester(url):
	return requests.get('https://blockchain.info/rawaddr/' + url).text