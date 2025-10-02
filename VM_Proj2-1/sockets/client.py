import socket
import signal
import sys
import datetime
import struct

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "cibersecurity.com"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

while True:
    try: 
        message=input("Request to send? ")
        if message!="ip" or message!= "hostname" or message != "bytes" or message != "total": 
            print("Not recognized operation, try again!")
            continue
        sock.send(message.encode())
        response = sock.recv(1024)
        print("Server-> {}".format(response.decode()))
    except(socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)

