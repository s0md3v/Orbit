#!/usr/bin/env python3

import threading
import json
import random
import urllib3
from time import sleep
from re import findall
urllib3.disable_warnings()
http = urllib3.PoolManager()

addrs_1 = set()
addrs_2 = set()
addrs_3 = set()
edges = []

database = {}

api = 'https://blockchain.info/rawaddr/'

white = '\033[97m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'
back = '\033[7;91m'
info = '\033[93m[!]\033[0m'
que = '\033[94m[?]\033[0m'
bad = '\033[91m[-]\033[0m'
good = '\033[32m[+]\033[0m'
run = '\033[97m[~]\033[0m'

print ('''%s
  __         
 |  |  _ |  ' _|_
 |__| |  |) |  |  
%s''' % (green, end))

main = input('%s Enter a wallet address: ' % que)

database[main] = {}
database[main]['nSize'] = 0
database[main]['eTo'] = {}

def requester(url, addrs_y):
    response = http.request('GET', api + url).data
    matches = findall(r'"addr":".*?"', str(response))
    for match in matches:
        found = match.split('"')[3]
        if found in database:
            database[found]['nSize'] += 1
        else:
            database[found] = {}
            database[found]['nSize'] = 0
            database[found]['eTo'] = {}
        if found not in database[url]['eTo']:
            database[url]['eTo'][found] = 0
        else:
            database[url]['eTo'][found] += 1
        database[url]['nSize'] += 1
        addrs_y.add(found)

def threader(urls, addrs_y):
    threads = []
    for url in urls:
        task = threading.Thread(target=requester, args=(url, addrs_y))
        threads.append(task)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    del threads[:]

def flash(addrs_x, addrs_y):
    begin = 0
    end = 4
    for i in range((int(len(addrs_x)/4)) + 1):
        threader(list(addrs_x)[begin:end], addrs_y)
        begin += 4
        if (len(addrs_x) - end) >= 4:
            end += 4
        else:
            end += len(addrs_x) - begin

threader([main], addrs_1)
print ('%s %i wallets found from %s wallet.' % (good, len(addrs_1), 1))
print ('%s Estimated time to crawl: %i seconds' % (info, len(addrs_1) * 2))
flash(addrs_1, addrs_2)
print ('%s %i wallets found from %i wallets' % (good, len(addrs_2), len(addrs_1)))
print ('%s Estimated time to crawl: %i seconds' % (info, len(addrs_2) * 6))
flash(addrs_2, addrs_3)
print ('%s %i wallets found from %i wallets' % (good, len(addrs_3), len(addrs_2)))
jsoned = {'edges':[],'nodes':[]}
num = 1

print ('%s Total unique btc addresses found: %i' % (good, len(database)))

for node in database:
    x, y = random.randint(1, 800), random.randint(1, 500)
    x, y = random.choice([x, x * -1]),random.choice([y, y * -1])
    jsoned['nodes'].append({'label': node, 'x': x, 'y': y, 'id':'id=' + node, 'size':database[node]['nSize']})
    for dest in database[node]['eTo']:
        if node != dest:
            size = database[node]["eTo"][dest]
            jsoned['edges'].append({'source':'id=' + node,'target':'id=' + dest,'id':num,"size":size})
        num += 1
render = json.dumps(jsoned).replace(' ', '')

new = open('%s.json' % main, 'w+')
new.write(render)
new.close()
