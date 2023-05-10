import socket
from threading import Thread
from tkinter import *

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipAdr="127.0.0.1"
port=8000
client.connect((ipAdr,port))

print("Connected With The Server")

class GUI :
    def __init__(self) :
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.Pls=Label(self.login,text="Please login to continue",justify=CENTER,font="Helvetica 14 bold")
        self.Pls.place(relheight=0.15,relx=0.2,rely=0.07)
        self.labelName=Label(self.login,text="Name:",font="Helvetica 14")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)
        self.entryname=Entry(self.login,font="Helvetica 14")
        self.entryname.place(relheight=0.12,relx=0.35,rely=0.2,relwidth=0.4)
        self.entryname.focus()
        self.go=Button(self.login,text="CONTINUE",font="Helvetica 14 bold",command=lambda: self.goAhead(self.entryname.get()))
        self.go.place(relx=0.4,rely=0.55)

        self.Window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.recieve)
        rcv.start()


    def recieve(self):
        while True :
            try :
                message=client.recv(2048).decode("utf-8")
                if message=="NICKNAME":
                    client.send(self.name.encode("utf-8"))
                else :
                    pass
            except:
                print("An error occured")
                client.close()
                break
g=GUI()

#  def write():
#     while True :
#         message="{}: {}".format(nickname,input(""))
#         client.send(message.encode("utf-8"))

# receiveThread=Thread(target=recieve)
# receiveThread.start()
# writeThread=Thread(target=write)
# writeThread.start()
