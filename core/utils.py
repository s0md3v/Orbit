import random

def pageLimit(n):
    return int((round(n, 49)/49) + 1)

def round(n, m):
    r = n % m
    return n + m - r if r + r >= m else n - r

def ranker(database, top):
    newDatabase = {}
    for node in database:
        newDatabase[node] = {}
        topSize = [0 for i in range(top)]
        topAdd = ['' for i in range(top)]
        for each in database[node]:
            minimum = min(topSize)
            if database[node][each] > minimum:
                index = topSize.index(minimum)
                topSize[index] = database[node][each]
                topAdd[index] = each
        for size, address in zip(topSize, topAdd):
            newDatabase[node][address] = size
    return newDatabase

def genLocation():
    x, y = random.randint(1, 800), random.randint(1, 500)
    x, y = random.choice([x, x * -1]), random.choice([y, y * -1])
    return x, y

def getNew(database, processed):
    new = []
    for address in database:
        if address not in processed:
            new.append(address)
        for childAddress in database[address]:
            if childAddress not in processed:
                new.append(childAddress)
    return set(filter(None, new))