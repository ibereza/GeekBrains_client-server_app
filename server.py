import argparse
import re
from socket import *
from time import time

from variables import DEFAULT_PORT
from utilities import send_message, get_message


def get_cli_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-a", type=str, default='', help='Listening IP')
    args_parser.add_argument("-p", type=int, default=DEFAULT_PORT, help='TCP port')
    args = args_parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    if args.a != '' and re.match(ip_re_tpl, args.a) is None:
        print('Please enter a valid IP address')
        exit(1)
    if not 1024 <= args.p <= 65535:
        print('The port address must be in the range 1024-65535')
        exit(1)
    return args.a, args.p


def connect_server_socket(ip, port):
    socket_ = socket(AF_INET, SOCK_STREAM)
    try:
        socket_.bind((ip, port))
    except OSError:
        print(f'Address {ip} or port {port} already in use')
        exit(1)
    socket_.listen(5)
    print(f'Server started on port {port}')
    return socket_


def main():
    ip, port = get_cli_args()
    server_socket = connect_server_socket(ip, port)

    while True:
        client, address = server_socket.accept()
        print(f"Connection request received from {address}")

        client_message = get_message(client)
        print(f'Message received: {client_message}')

        server_message = ''
        if client_message['action'] == 'presence':
            server_message = {
                "response": 200,
                "time": time(),
                "alert": 'OK'
            }
        send_message(client, server_message)

        client.close()


if __name__ == '__main__':
    main()
