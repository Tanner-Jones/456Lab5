import socket
import time


#initiates udp IPs and ports
TCP_IP = socket.gethostname()
TCP_PORT_RECEIVE = 5005
TCP_PORT_SEND = 4444

#creates socket object for UDP receive
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # UDP
sock.bind((TCP_IP, TCP_PORT_RECEIVE))

#initialize empty list for received messages
message_list = []


def accept_file(conn):
    time.sleep(1)
    conn.sendall(b'Message Accepted')
    output = open("output.txt", 'wb')
    time.sleep(1)
    while True:
        data = conn.recv(1024)
        if data:
            output.write(data)
            print(data)
        else:
            time.sleep(1)
            conn.sendall(b'File received successfully')
            break

def decline_file(conn):
    time.sleep(1)
    conn.sendall(b'Message Rejected')



while True:
    #Loop to wait for received messages
    sock.listen()
    conn, addr = sock.accept()

    data = conn.recv(1024)
    fileName = str(data)
    time.sleep(1)
    accept = input("Client attempting to send file:" + str(data,encoding='utf8') + "\nAccept file? Y/N")
    if accept == "Y":
        accept_file(conn)
    else:
        decline_file(conn)










