import requests
from requests.exceptions import BaseHTTPError, HTTPError
from getpass import getpass

try:
    url = 'https://api.github.com/search/users'

    data = {'q' : 'danxx26Hub'}
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}

    response = requests.get(url, params=data, headers=headers)

    json_response = response.json()
    print(json_response['items'][0]['url'])
    url2 = json_response['items'][0]['url']
    response2 = requests.get(url2)

    json_data = response2.json()
    for (k, v) in json_data.items():
        print(f"{k} : {v}")
except HTTPError as e:
    print(e)
except KeyError as k:
    print(k)