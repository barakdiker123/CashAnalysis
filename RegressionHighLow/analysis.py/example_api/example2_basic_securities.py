#!/usr/bin/env python3

import http.client

conn = http.client.HTTPSConnection("openapigw.tase.co.il")

headers = {
    "Authorization": "Bearer AAIgNDI2MjMzZmY0NGQ3Yjg5MmM2OGJmYzI3MTUwNTRmZjhKA_4TnMGNJIxh5l1XEDZLsXYLRrErHuAWniNxZlJk7A-lhZ3qc8B1RkAdmhRwZ1jS_qGvBZCW-PLwnNFVOZ-LjplGe7GM3Ph60z5mJCrAfBbBKWjvBMTaOq6iRZaON3c",
    "accept-language": "he-IL",
    "accept": "application/json",
}

conn.request(
    "GET",
    "/tase/prod/api/v1/basic-securities/trade-securities-list/2020/4/23",
    headers=headers,
)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
