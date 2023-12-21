import time
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.1.23', 1234)
    server_socket.bind(addr)
    server_socket.listen()
    print(f'server started at {addr}')
    while True:
        # wait for clients to connect
        client_socket, client_addr = server_socket.accept()
        Thread(target=handle_client,
               args=(client_socket, client_addr)).start()


def handle_client(client_socket, client_addr):
    print(f'Got a connection from {client_addr}')
    username = client_socket.recv(1024).decode('ascii')
    msg = f'hello {username} and welcome to python networking'
    time.sleep(10)
    client_socket.send(msg.encode('ascii'))
    print('client socket is being closed.')


if __name__ == '__main__':
    main()
