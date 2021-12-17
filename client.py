PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
import socket
PORT = 5050
SERVER = '192.168.15.221'
ADDR = (SERVER, PORT)
HEADER=64
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet.connect(ADDR)
def send(msg):
     message=msg.encode('utf-8')
     msg_length=len(message)
     send_length=str(msg_length).encode('utf-8')
     send_length += b''*(HEADER-len(send_length))
     client.send(message)


