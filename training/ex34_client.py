from socket import socket, AF_INET, SOCK_STREAM


def main():
    print('client started')
    client_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.1.23', 1234)
    client_socket.connect(addr)
    print(f'connected to {addr} successfully')
    print('end of client app')


if __name__ == '__main__':
    main()
