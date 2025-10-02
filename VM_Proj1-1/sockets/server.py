import socket
import threading
import signal
import sys
import struct

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##
clients={}
nbytes=0


def handle_client_connection(client_socket,address): 
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    clients['{},{}'.format(address[0],address[1])]=0
    try:
        while True:
            request = client_socket.recv(1024)
            if not request:
                client_socket.close()
            else:
                message= request.decode()
                print('Received {}'.format(message))
                clients['{},{}'.format(address[0],address[1])]+=len(request)

            if message == 'hostname':
                response = "hostname: {}".format(socket.gethostname())
            elif message == 'ip':
                response = "ip: {}".format(socket.gethostbyname(socket.gethostname()))
            elif message == 'bytes':
                response = "bytes: {}".format(clients['{},{}'.format(address[0],address[1])])
            elif message == 'total':
                response = "total: {}".format(sum(clients.values()))
            else:   
                message="Not recognized operation try again!"

            client_socket.send(response.encode())
            
    except(socket.timeout, socket.error):
        print('Client {} error. Done!'.format(address))

ip_addr= "0.0.0.0"
tcp_port = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_addr, tcp_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(ip_addr, tcp_port))

while True:
    client_sock, address = server.accept()
    client_handler = threading.Thread(target=handle_client_connection,args=(client_sock,address),daemon=True)
    client_handler.start()