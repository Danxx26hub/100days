from datetime import datetime
import schedule


__author__ = 'danxx26@gmail'

def main():
    
    print_header()

    today = datetime.today().day
    month = int(input('please enter month [MM] '))
    day = int(input('please enter a date [DD]'))
    
    if event_time(today, month, day):
        print(f'your event is {event_time(today, month, day)} from today')


def print_header():
    print('-' * 30)
    print('   Event Timer          ')
    print('   enter your Month / Date ')
    print('-' * 30)
    print()

def event_time(today, month, day):
    today = datetime.today()
    event = datetime(2019, month, day)
    if event.date() == today.date():
        print('Your event is today!!!!')
        return None
    else:
        event_date = (event - today)
        return event_date

    


if __name__ == '__main__':
    schedule.every(24).hours.do(main())


    
