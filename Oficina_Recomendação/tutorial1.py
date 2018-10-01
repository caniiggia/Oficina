#!/usr/bin/python3

# Structure of the .json with interactions:

#[
#   {"user_id": "user-50",  "item_id": "event-276", "timestamp": "2016-04-20T12:50:42+02:00"},
#   {"user_id": "user-389", "item_id": "event-73",  "timestamp": "2014-07-20T02:49:45+02:00"},
#  {"user_id": "user-204", "item_id": "event-116", "timestamp": "2015-04-22T13:32:32+02:00"},

# ]

from recombee_api_client.api_client import *
from recombee_api_client.api_requests import *
import json

client = RecombeeClient('foundanies', 'VIqQZQ7GPEsESMjS41PIc2zhE4fpWDA2vj6KnJwUBkyblWARDAYz3NNbYzxCwqtW')

requests = []

with open('purchases.json') as f:
    interactions = json.loads(f.read())
    for interaction in interactions:
        r = AddPurchase(interaction['user_id'],
                        interaction['item_id'],
                        timestamp=interaction['timestamp'],
                        cascade_create=True)
        requests.append(r)

br = Batch(requests)
client.send(br)

recommended = client.send(RecommendItemsToUser('user-50', 2))
print(recommended)

recommended = client.send(RecommendItemsToItem('event-50', 'user-204', 2))
print(recommended)

recommended = client.send(RecommendUsersToItem('event-389', 2))
print(recommended)

