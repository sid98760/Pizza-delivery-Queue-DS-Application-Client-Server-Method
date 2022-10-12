# GROUP 2 INTERNAL PROJECT FOR DATA STRUCTURES
# TITLE: REAL TIME APPLICATIONS OF QUEUE
# GROUP MEMBERS:
# 4211 : RAHUL CHIBDE
# 4212 : SIDDHESH CHINCHOLE
# 4213 : RASHI CHOPDEKAR
# 4214 : SHARVIN DESAI

# SERVER INTERFACE FOR PIZZA HOUSE

# IMPORTING MODULES
import socket
from tkinter import *

# DECLARING VARIABLES AS GLOBAL
global msg

# CREATING A SOCKET FOR RECEIVING THE ORDER FROM CLIENT
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created")
s.bind((socket.gethostname(), 1250))

s.listen(10)
print("Waiting for Connections")

while True:
    pizza_house, address = s.accept()
    print("Connected with", address)
    while True:
            # RECEIVING THE ACTUAL ORDER DATA FROM CLIENT
            msg = pizza_house.recv(1024).decode()
            if msg:
                print(msg)
                # REPLACING THE OTHER ELEMENTS AS DATA WAS RECEVIED IN STRING
                msg1 = msg.replace("[[", "")
                msg2 = msg1.replace("]]", "")
                msg3 = msg2.replace("[", "")
                msg4 = msg3.replace("]", "")
                msg5 = msg4.replace("'", "")

                print(msg5)

                # CONVERTING OUR DATA INTO LISTS
                global new_msg
                new_msg = msg5.split(",")
                print(new_msg)

                for i in new_msg:
                    print(i)

                # CREATING 1st WINDOW FOR SERVER INTERFACE
                window1 = Tk()
                window1.title("Pizza House Management")
                window1.geometry("500x500")

                # FUNCTION FOR VIEWING THE ORDER
                def vieworder():

                    # CREATING THE 2nd WINDOW OF SERVER INTERFACE FOR VIEWING THE ORDER
                    window2 = Tk()
                    window2.title("View the Order")
                    window2.geometry("500x500")

                    # FUNCTION FOR QUITING THE WINDOW
                    def quit():
                        window1.destroy()

                    # FUNCTION FOR DELETING THE FIRST ORDER AFTER VIEWING IT
                    def neworder():
                        if len(new_msg) != 0:
                            new_msg.pop(0)
                            new_msg.pop(0)
                            new_msg.pop(0)
                            new_msg.pop(0)
                            new_msg.pop(0)
                            new_msg.pop(0)
                            window2.destroy()

                    # GUI INTERFACE FOR DISPLAYING EACH ORDER INDIVDULLY
                    if len(new_msg) != 0:
                        label1 = Label(window2, text="American Pizza:", font=("Calibri", 13)).place(x=30, y=50)
                        label11 = Label(window2, font=("Calibri", 13), text=new_msg[0], bg="white", fg="black").place(x=230, y=50)

                        label2 = Label(window2, text="Number of American Pizza:", font=("Calibri", 13)).place(x=30,y=100)
                        label12 = Label(window2, font=("Calibri", 13), text=new_msg[1], bg="white", fg="black").place(x=230, y=100)

                        label3 = Label(window2, text="Desi pizza:", font=("Calibri", 13)).place(x=30, y=150)
                        label13 = Label(window2, font=("Calibri", 13), text=new_msg[2], bg="white", fg="black").place(x=230, y=150)

                        label4 = Label(window2, text="Number of Desi Pizza:", font=("Calibri", 13)).place(x=30, y=200)
                        label14 = Label(window2, font=("Calibri", 13), text=new_msg[3], bg="white", fg="black").place(x=230, y=200)

                        label5 = Label(window2, text="Name:", font=("Calibri", 13)).place(x=30, y=250)
                        label15 = Label(window2, font=("Calibri", 13), text=new_msg[4], bg="white", fg="black").place(x=230, y=250)

                        label6 = Label(window2, text="Address:", font=("Calibri", 13)).place(x=30, y=300)
                        label16 = Label(window2, font=("Calibri", 13), text=new_msg[5], bg="white", fg="black").place(x=230, y=300)

                        button2 = Button(window2, height=1, width=15, font=("Calibri", 13, "bold"), text="close",command=neworder, bg="black", fg="white").place(x=180, y=350)

                    # GUI INTERFACE IF THERE ARE NO NEW ORDERS
                    else:
                        window3 = Tk()
                        window3.title("New Message")
                        window3.geometry("350x100")
                        label_new = Label(window3, text="No new orders right now", font=("Calibri", 13)).place(x=30,y=40)
                        window2.destroy()

                # BUTTONS ON 1st WINDOW FOR VIEWING THE ORDER AND EXITING IT
                button1 = Button(window1, height=1, width=15, font=("Calibri", 13, "bold"), text="View Order",command=vieworder, bg="black", fg="white").place(x=180, y=100)

                button3 = Button(window1, height=1, width=15, font=("Calibri", 13, "bold"), text="EXIT", command=exit,bg="black", fg="white").place(x=180, y=300)

                window1.mainloop()

    # CLOSING OUR SOCKET
    pizza_house.close()





