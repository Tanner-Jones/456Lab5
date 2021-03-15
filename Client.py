import socket
import sys


TCP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
TCP_PORT_SEND = 5005
TCP_PORT_RECEIVE = 4444

while True:
    fileName = sys.argv[2]
    MESSAGE = bytes(fileName, encoding='utf8')


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT_SEND))
    sock.sendall(MESSAGE)
    data = sock.recvfrom(1024)
    if data[0] == b'Message Accepted':
        file = open(fileName, 'rb')
        print(file.read())
        while len(full_file) > 0:
            message = bytes(full_file[0:1023])
            sock.sendall(message)
            full_file = full_file[1024:]
    else:
        print("Message was rejected, try again later please")

