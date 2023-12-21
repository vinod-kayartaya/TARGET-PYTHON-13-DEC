from socket import socket, AF_INET, SOCK_STREAM


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.1.23', 1234)
    server_socket.bind(addr)
    server_socket.listen()
    print(f'server started at {addr}')
    while True:
        # wait for clients to connect
        client_socket, client_addr = server_socket.accept()
        print(f'Got a connection from {client_addr}')


if __name__ == '__main__':
    main()
