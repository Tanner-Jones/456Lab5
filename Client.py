import socket
import sys


TCP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
TCP_PORT_SEND = 5005
TCP_PORT_RECEIVE = 4444

while True:
    fileName = sys.argv[2]
    MESSAGE = bytes(fileName, encoding='utf8')


    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # UDP
    sock.connect((TCP_IP, TCP_PORT_SEND))
    sock.sendall(MESSAGE)

    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.bind((HOSTNAME, TCP_PORT_RECEIVE))
    sock2.listen()
    conn, addr = sock2.accept()
    data = conn.recvfrom(1024)
    if data == b'Message Accepted':
        file = open(fileName, 'rb')
        full_file = bytearray(file)
        while len(full_file) > 0:
            message = bytes(full_file[0:1023])
            sock.sendall(message)
            full_file = full_file[1024:]
    else:
        print("Message was rejected, try again later please")

