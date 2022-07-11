import requests

url = 'http://localhost:8000/api/'

res = requests.post(url, params = {'salary': 200}, json = {'description': 'post description 4', 'price': 3.99})

print(res.json())