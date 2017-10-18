import requests

headers = {'Host': 'web'}

for x in range (1, 100000):
    r = requests.get('http://localhost:4140/', headers=headers)


    print r.content, x