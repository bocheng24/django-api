import requests

url = 'http://localhost:8000/api/'

res = requests.get(url, params = {'salary': 200}, json = {'q': 'one query'})

print(res.json())