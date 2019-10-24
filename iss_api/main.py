import requests


url = "http://api.open-notify.org/astros.json"
headers = {'Content-Type' : 'text/json'}
response = requests.get(url, headers=headers)
print(response)
