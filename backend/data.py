import requests
import json

response = requests.get('https://api.enco.io/swagger/cloe/1.0.0')
print(response.status_code)

data = response.json()
print(data)
