import socket
from threading import Thread  

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipAdr="127.0.0.1"
port=8000
server.bind((ipAdr,port))
server.listen()
clients=[]

nicknames=[]

print("Server is running")

def clientthread(conn,nickname):
    conn.send("Welcome To This Chat Room".encode("utf-8"))
    
    while True:
        try:
            msg=conn.recv(2048).decode("utf-8")
            if msg:
                print(msg)
     
                broadcast(msg,conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue

def broadcast(message,reciever):
    for client in clients:
        if client!=reciever:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)
def remove(reciever):
    if reciever in clients:
        clients.remove(reciever)

def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    conn,adr=server.accept()
    conn.send("NICKNAME".encode("utf-8"))
    nickname=conn.recv(2048).decode("utf-8")
    clients.append(conn)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message,conn)
    newThread=Thread(target=clientthread,args=(conn,adr))
    newThread.start()