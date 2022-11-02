import tkinter
import socket
from tkinter import *
from threading import Thread

def receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("Error")

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))
    if msg== "#quit":
        s.close()
        window.close()

def on_closing():
    my_msg.set("#quit")
    send()

window = Tk()
window.title("Chat room app")
window.configure(bg="yellow")
message_frame = Frame(window, height=100, width=100, bg="white")
message_frame.pack()
my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=10, width=80, bg="white", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label_1 = Label(window, text="Enter the Message", fg="black", font="Arial", bg="yellow")
label_1.pack()

entry_text = Entry(window, textvariable=my_msg, fg="black", width=50)
entry_text.pack()

send_button = Button(window, text="Send", font="Arial", fg="black", command=send)
send_button.pack()

quit_button = Button(window,text="Quit", font="Arial", fg="black", command=on_closing)
quit_button.pack()

Host= "127.0.0.1"
Port=8000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,Port))
receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()