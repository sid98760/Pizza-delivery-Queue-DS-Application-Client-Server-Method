# GROUP 2 INTERNAL PROJECT FOR DATA STRUCTURES
# TITLE: REAL TIME APPLICATIONS OF QUEUE
# GROUP MEMBERS:
# 4211 : RAHUL CHIBDE
# 4212 : SIDDHESH CHINCHOLE
# 4213 : RASHI CHOPDEKAR
# 4214 : SHARVIN DESAI

# CLIENT INTERFACE FOR PIZZA HOUSE

# IMPORTING MODULES
from tkinter import *
import socket

# CREATING 1st WINDOW OF CLIENT INTERFACE
root = Tk()
root.title("Pizza")
root.geometry("500x500")
root.config(bg="white")

# DECLARING VARIABLES AND QUEUES (in from of lists)
global order_queue
order_queue = []
global pizza

# EXIT FUNCTION
def exit():
    root.destroy()

# FUNCTION FOR ORDERING PIZZA OF OWN CHOICE
def order():
    # CREATING 2nd WINDOW OF CLIENT INTERFACE
    window = Tk()
    window.title("Order a Pizza")
    window.geometry("500x500")

    # FUNCTION FOR CONFIRMING THE AMERICAN PIZZA
    def flash1():
        entry1.delete(0,'end')
        choose1 = listbox1.get(ANCHOR)
        entry1.insert(0,american[choose1])

    # FUNCTION FOR CONFIRMING THE DESI PIZZA
    def flash2():
        entry2.delete(0, 'end')
        choose2 = listbox2.get(ANCHOR)
        entry2.insert(0, indian[choose2])

    # FUNCTION FOR ADDING ORDER DETAILS IN QUEUE AND CONFIRMING THE ORDER
    def submit():
        pizza = []
        pizza.append(entry1.get())
        pizza.append(entry5.get())
        pizza.append(entry2.get())
        pizza.append(entry6.get())
        pizza.append(entry3.get())
        pizza.append(entry4.get())
        print(pizza)
        order_queue.append(pizza)
        print(order_queue)
        window.destroy()

        # FUNCTION FOR CREATING A SOCKET AND SEND INFORMATION TO SERVER
        def ok():
            window1.destroy()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket Created")
            s.connect((socket.gethostname(), 1250))
            print("Connected")

            new_order = str(order_queue)
            s.send(bytes(new_order, "utf-8"))

            s.close()

        # CREATING THE 3rd WINDOW OF CLIENT INTERFACE TO CONFIRM THE ORDER
        window1= Tk()
        window1.title("Confirm Your Order")
        window1.geometry("350x100")
        confirm = Label(window1,text="Your Order has been placed in a Queue.\nWould You Like to Order anything else?",font=("Calibri",10))
        confirm.place(x=10,y=10)
        confirm_b = Button(window1,text="Confirm",command=ok).place(x=290,y=70)
        order_b = Button(window1,text="Order",command=order).place(x=240,y=70)






    # MENU CARD OF AMERICAN PIZZA IN FORM OF TUPPLES
    american = {
        '1 Margerita Pizza        : ₹205':'Margerita Pizza        : ₹205',
        '2 Vegeterian Bite        : ₹295':'Vegeterian Bite        : ₹295',
        '3 Mushroom Riot          : ₹315':'Mushroom Riot          : ₹315',
        '4 Mexican Delight        : ₹345':'Mexican Delight        : ₹345',
        '5 Mexican Chilli Combo   : ₹350':'Mexican Chilli Combo   : ₹350',
        '6 Chicken Cheeze Burst   : ₹360':'Chicken Cheeze Burst   : ₹360',
        '7 Chicken Chilly Passion : ₹375':'Chicken Chilly Passion : ₹375',
        '8 Texas BBQ              : ₹400':'Texas BBQ              : ₹400',
    }

    # MENU CARD OF DESI PIZZA IN FORM OF TUPPLES
    indian = {
        '1 Tandoori Panner        : ₹205':'Tandoori Panner        : ₹205',
        '2 Cheeze Panner Tandoori : ₹220':'Cheeze Panner Tandoori : ₹220',
        '3 Chatpata Panner        : ₹250':'Chatpata Panner        : ₹250',
        '4 Chatpata Panner        : ₹250':'Chatpata Panner        : ₹250',
        '5 Tandoori Chicken       : ₹300':'Tandoori Chicken       : ₹300',
        '6 Chicken Cheeze Tandoori: ₹330':'Chicken Cheeze Tandoori: ₹330',
        '7 Cheeze Chilly Chicken  : ₹350':'Cheeze Chilly Chicken  : ₹350',
        '8 Chicken Kheema Spread  : ₹375':'Chicken Kheema Spread  : ₹375',
    }

    # ADDING THE MENU CARD OF AMERICAN PIZZA IN LISTBOX
    listbox1 = Listbox(window,width=30,height=8)
    for x,y in enumerate(american):
        listbox1.insert(x+1,y)
    listbox1.pack(anchor='w',pady=70,padx=30)

    # ADDING THE MENU CARD OF DESI PIZZA IN LISTBOX
    listbox2 = Listbox(window,width=30,height=8)
    listbox2.place(x=300, y=70)
    for x,y in enumerate(indian):
        listbox2.insert(x+1,y)

    # GUI FOR ORDERING THE PIZZA OF OWN CHOICE IN THE 2nd WINDOW OF CLIENT INTERFACE
    button1 = Button(window,text="Confirm",command=flash1)
    button1.place(x=30, y=200)

    button2 = Button(window, text="Confirm", command=flash2)
    button2.place(x=300, y=200)


    entry1 = Entry(window, width=30)
    entry1.place(x=30, y=50)

    entry2 = Entry(window, width=30)
    entry2.place(x=300, y=50)

    label1 = Label(window,text="Name:",font=('Calibri',12,"bold"))
    label1.place(x=30,y=275)

    entry3 = Entry(window,width=30)
    entry3.place(x = 30, y= 300)

    label2 = Label(window, text="Address:", font=('Calibri', 12,"bold"))
    label2.place(x=30, y=350)

    entry4 = Entry(window,width=40)
    entry4.place(x=30, y=375)

    label3 = Label(window, text="Number of selected American Pizza", font=('Calibri', 10))
    label3.place(x=300, y=250)

    entry5 = Entry(window, width=5)
    entry5.place(x=300, y=275)

    label4 = Label(window, text="Number of selected Desi Pizza", font=('Calibri', 10))
    label4.place(x=300, y=300)

    entry6 = Entry(window, width=5)
    entry6.place(x=300, y=325)

    label5 = Label(window,text="AMERICAN PIZZA's",font=("Source Sans Pro",12),width=20)
    label5.place(x=29, y=25)

    label6 = Label(window, text="DESI PIZZA's", font=("Source Sans Pro", 12), width=20)
    label6.place(x=300, y=25)

    submit_button = Button(window,text="Place the order",command=submit,font=("calibri",15,"bold"))
    submit_button.place(x=180, y=420)

    window.mainloop()

# GUI FOR PLACING THE ORDER BUTTON OR EXIT ON THE 1st WINDOW OF CLIENT INTERFACE
b_1 = Button(root,height=2,width=20,text="Place a Order",font=("Calibri",12,"bold"),bg="blue",command=order).place(x=175,y=100)

b_2 = Button(root,height=2,width=20,text="EXIT",font=("Calibri",12,"bold"),bg="blue",command=exit).place(x=175,y=300)


root.mainloop()






