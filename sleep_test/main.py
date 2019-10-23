import time
import requests 


def uptime_bot(url):
    while True:
        try:
            response = requests.get(url, timeout=6.0)
        except requests.ConnectionError:
            print(f'unable to connect to {url}')
        except requests.URLRequired:
            print(f'please enter a valid url :{url}')
        else:
            print(f'{url} is up {response}')
        time.sleep(60)


if __name__ == '__main__':
    url = 'https://www.googlecom'
    uptime_bot(url)
