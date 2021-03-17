import socket
import sys


TCP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
TCP_PORT_SEND = 5005
TCP_PORT_RECEIVE = 4444

while True:
    fileName = sys.argv[2]
    MESSAGE = bytes(fileName, encoding='utf8')

    # set up socket connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT_SEND))
    # send filename to ask on server side
    sock.sendall(MESSAGE)
    data = sock.recvfrom(1024)
    # if statement to handle whether server accepts or declines
    if data[0] == b'Message Accepted':
        file = open(fileName, 'rb')
        contents = file.read()
        full_file = bytearray(contents)
        # takes files as bytearray and splits it into 1024 bytes until message is empty
        while len(full_file) > 0:
            message = bytes(full_file[0:1024])
            sock.sendall(message)
            full_file = full_file[1024:]
        # once empty waits for acknowledgement and closes socket
        data = sock.recvfrom(1024)
        print(data[0].decode("utf-8"))
        sock.close()
        break
    else:
        # handles when server declines, prints a declined message and closes socket
        print("Message was rejected, try again later please")
        sock.close()
        break

