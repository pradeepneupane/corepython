import json
data = '{"var1": "Pradeep", "var2": 7}'
parsed = json.loads(data)
print(parsed['var1'])

data2 = {
    "channel_name" : "codewithpradeep",
    "cars" : ['bmw', 'audi a8', 'ferari'],
    "fridge" : ('roti', 420),
    "isbad" : False
}
jscomp = json.dumps(data2)
print(jscomp)
