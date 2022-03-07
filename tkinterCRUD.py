from cProfile import label
from cgi import test
from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("400x400")

l_id = Label(root, text="ID")
l_id.place(x=50, y=50)

l_ifname = Label(root, text="First Name")
l_ifname.place(x=50, y=100)

l_lname = Label(root, text="Last Name")
l_lname.place(x=50, y=150)

l_email = Label(root, text="Email")
l_email.place(x=50, y=200)

l_phone = Label(root, text="Phone Number")
l_phone.place(x=50, y=250)

e_id = Entry(root)
e_id.place(x=180, y=50)

e_fname = Entry(root)
e_fname.place(x=180, y=100)

e_lanme = Entry(root)
e_lanme.place(x=180, y=150)

e_email = Entry(root)
e_email.place(x=180, y=200)

e_phone = Entry(root)
e_phone.place(x=180, y=250)


root.mainloop()
