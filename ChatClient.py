from tkinter import *
import socket
import threading
import time

shutdown = False
def receiving(name,sock):
        while not shutdown:
            while True:
                #encode?
                data, addr = sock.recvfrom(1024)
                listbox.insert(END, data.decode('utf-8')+"\n")

def callback():

    global buttonClk
    global nickname
    global notConnected
    global s
    global server
    global comment
    if buttonClk:
        nickname = E1.get()
        E1.delete(0, 'end')
        buttonClk = False
        L1.config(text = "Comment")
    else:
        comment = E1.get()
        #listbox.insert(END, nickname+": " + comment+"\n")
        E1.delete(0, 'end')
        if notConnected:
            server = ('52.24.122.107', 5000)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((host,port))
            rT = threading.Thread(target=receiving, args=('RecvThread',s))
            rT.start()
            notConnected = False
        s.sendto(bytearray(str.encode(nickname + ': ' + comment)),server)

host = '52.24.122.107'
port = 5000

root = Tk()
listbox = Text(root, width = 40)
listbox.grid(rowspan = 10, columnspan = 10)
root.title("Team Jacob Chat Client")
L1 = Label(root, text="User Name")
L1.grid(row = 11, column= 1)
E1 = Entry(root, width = 30, bd = 5)
E1.grid(row = 11, column= 6)
buttonClk = True
notConnected= True
nickname = ""
MyButton1 = Button(root, text="Submit", width=10, command=callback)
MyButton1.grid(row = 11, column = 8)
root.mainloop()









