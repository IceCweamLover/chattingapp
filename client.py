FORMAT='utf-8'
PORT = 5050
import socket
PORT = 5050
SERVER = '192.168.15.221'
ADDR = (SERVER, PORT)
HEADER=64
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
