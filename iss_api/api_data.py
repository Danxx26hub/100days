import requests
from collections import namedtuple

def main():
    pass


def provide_endpoints():
    ''' place endpoint urls into namedtuple
    '''
    urls = ['astronauts', 'iss_pass', 'iss_now']
    api_endpoints = namedtuple("api_endpoints", urls)
    # crate endpoints namedtuple with all 3 api urls
    endpoints = api_endpoints('http://api.open-notify.org/astros.json',
                              'http://api.open-notify.org/iss-pass.json',
                              'http://api.open-notify.org/iss-now.json' 
                              )
    return endpoints


def get_astronauts(people):
    people = people
    response = requests.get(people)
    return response


if __name__=="__main__":
    main()
