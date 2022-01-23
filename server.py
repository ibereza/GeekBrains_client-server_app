import argparse
import json
import re
from socket import *
from time import time

PORT = 7777
MAX_MESSAGE_LEN = 1024


def get_cli_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-a", type=str, default='', help='Listening IP')
    args_parser.add_argument("-p", type=int, default=PORT, help='TCP port')
    args = args_parser.parse_args()
    print(args)
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    if args.a != '' and re.match(ip_re_tpl, args.a) is None:
        print('Please enter a valid IP address')
        exit()
    if not 1024 <= args.p <= 65535:
        print('The port address must be in the range 1024-65535')
        exit()
    return args.a, args.p


server_socket = socket(AF_INET, SOCK_STREAM)
ip_address, port = get_cli_args()
try:
    server_socket.bind((ip_address, port))
except OSError:
    print('Address or port already in use')
    exit()
server_socket.listen(5)
print(f'Server started on port {port}')

while True:
    client, address = server_socket.accept()
    print(f"Connection request received from {address}")

    data = client.recv(MAX_MESSAGE_LEN)
    client_message = json.loads(data.decode('utf-8'))
    print(f'Message received: {client_message}')

    server_message = ''
    if client_message['action'] == 'presence':
        server_message = {
            "response": 200,
            "time": time(),
            "alert": 'OK'
        }

    data = json.dumps(server_message).encode('utf-8')
    client.send(data)

    client.close()
