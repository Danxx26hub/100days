import ssl
import sys
from librouteros import connect
import subprocess



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
con = connect(
    username='test',
    password='New@yellow22',
    host='192.168.88.1',
    ssl_wrapper=ctx.wrap_socket,
    port=8729
    )

s = True
while s:
    print('select options:\n')

    choice = input("""select I for system info,
                     H for health status, 
                     L for log, P for system profile, 
                     X to exit:\n""".center(50))

    print()
    choice = choice.lower()
    if choice == "h":
        print("getting health info")
        command = {'p': 'print'}
        health = con(cmd="/system/health/print")
        for stats in health:
            for voltage, temp in stats.items():
                voltage = stats.get('voltage')
                temp = stats.get('temperature')
                if temp > 47:
                    print("too hot shutting down router!!")

                else:
                    print(f"voltage is {voltage}")
                    print(f"temp is fine .... {temp} degrees")
                    #con(cmd="/system/reboot")
    elif choice == "l":
        print("reading logs")
        logs = con(cmd='/log/print')
        for log in logs:
            topics = log.get('topics')
            time = log.get('time')
            message = log.get('message')
            if topics != 'firewall,info':
                print(f"{topics} : {time} : {message}")
            else:            
                continue
    elif choice == 'p':
        print('running CPU / Memory profile\n')
        print('please wait.......')
        
        profiles = con(cmd="/tool/profile", duration='10', cpu='all')
        for profile in profiles:
            device = profile.get('name')
            usage = profile.get('usage')
            print(f'{device} : {usage}')
        print("Done!")
        print()
    elif choice == 'i':
        print('getting device info:\n')
        system_info = con(cmd="/system/resource/print")
        for sys_item in system_info:
            for k, v in sys_item.items():
                print(k, ' : ', v)
    else:
        print('exiting program')
        s = False



