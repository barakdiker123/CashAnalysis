

import http.client

conn = http.client.HTTPSConnection("openapigw.tase.co.il")

headers = {
    'Authorization': "Bearer AAIgNDI2MjMzZmY0NGQ3Yjg5MmM2OGJmYzI3MTUwNTRmZjhl8_2Fy7NHGOnzTQJVqXaCLSHuepfTzBjl5_TBcF54gAm1FSwbmZgla4A1f1bm9fxje5CAe4kmL7FYVR0G5llCNZD0u5zKGLIHmrsVAEnzK4Em7alGjj1SehzPIralVNk",
    'accept-language': "he-IL",
    'accept': "application/json"
    }

conn.request("GET", "/tase/prod/api/v1/basic-indices/index-components-basic/142/2020/11/10", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
