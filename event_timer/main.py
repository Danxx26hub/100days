from datetime import datetime

__author__ = 'danxx26@gmail'

def main():
    today = datetime.today().day
    month = int(input('please enter month [MM] '))
    day = int(input('please enter a date [DD]'))
    
    print(f'your event is {event_time(today, month, day)} from today')

def event_time(today, month, day):
    today = datetime.today()
    event = datetime(2019, month, day)
    event_date = (event - today)

    return event_date

    


if __name__ == '__main__':
    main()


    
