import socket
import time
import sys

def main():
    printBanner()
    ask = ask_input()
    ip = ask.get('ip')
    port = ask.get('port')
    isOpen(ip, port)
    print('done!')

    


def printBanner():
    print('-' * 40)
    print('|          IP Port Checker             |')
    print('-' * 40)


def ask_input():
    sock = {}
    ip = input('Please enter IP address:\n')
    port = input('Please enter port:\n')
    sock['ip'] = ip
    sock['port'] = port 
    return sock 

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
    
        s.connect((ip, int(port)))
        print(f' {ip} : {port} is up!')

    
    except OSError:
        print('port is not open or ip is down')
        time.sleep(1)
        sys.exit()
    finally:
    
        s.shutdown(socket.SHUT_RDWR)
        s.close()

if __name__ == '__main__':
    main()
