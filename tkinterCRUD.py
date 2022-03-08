from cProfile import label
from cgi import test
from tkinter import *
import tkinter.messagebox as msg
import mysql.connector as sqlConn


def createConnection():
    return sqlConn.connect(
        host="localhost",
        user="root",
        password="",
        database="python_gui"
    )

# print(createConnection())


def emptyEntry():
    if e_fname.get() == "" or e_lname.get() == "" or e_email.get() == "" or e_phone.get() == "":
        return True
    return False


def flushEntry(id=False):
    if not id:
        e_id.delete(0, 'end')
    e_fname.delete(0, 'end')
    e_lname.delete(0, 'end')
    e_email.delete(0, 'end')
    e_phone.delete(0, 'end')


def insertData():
    if emptyEntry():
        msg.showinfo("Insert Status", "All Fields are Mandatory")
    else:
        conn = createConnection()
        cursor = conn.cursor()
        query = "insert into information(fname, lname, email, phone) values(%s, %s, %s, %s)"
        args = (e_fname.get(), e_lname.get(), e_email.get(), e_phone.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        flushEntry()
        msg.showinfo("Insert Status", "Data Inserted Successfully")


def searchData():
    flushEntry(True)
    if e_id.get() == "":
        msg.showinfo("Search Status", "ID is Mandatory")
    else:
        conn = createConnection()
        cursor = conn.cursor()
        query = "select * from information where id = %s"
        args = (e_id.get(),)
        cursor.execute(query, args)
        data = cursor.fetchall()
        print(data)
        if(data == []):
            # print("empty")
            msg.showinfo("Search Status", "Not a Valid ID")
        else:
            for i in data:
                e_fname.insert(0, i[1])
                e_lname.insert(0, i[2])
                e_email.insert(0, i[3])
                e_phone.insert(0, i[4])
        conn.close()


def updateData():
    if emptyEntry() and e_id.get() == "":
        msg.showinfo("Update Status", "All Fields are Mandatory")
    else:
        conn = createConnection()
        cursor = conn.cursor()
        query = "update information set fname=%s, lname=%s, email=%s, phone=%s where id=%s"
        args = (e_fname.get(), e_lname.get(),
                e_email.get(), e_phone.get(), e_id.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        flushEntry()
        msg.showinfo("Update Status", "Data Updated Successfully")


def deleteData():
    if e_id.get() == "":
        msg.showinfo("Delete Status", "ID is Mandatory")
    else:
        conn = createConnection()
        cursor = conn.cursor()
        query = "delete from information where id=%s"
        args = (e_id.get(), )
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        flushEntry()
        msg.showinfo("Delete Status", "Data Deleted Successfully")


root = Tk()
root.title("TKINTER CRUD")
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

e_lname = Entry(root)
e_lname.place(x=180, y=150)

e_email = Entry(root)
e_email.place(x=180, y=200)

e_phone = Entry(root)
e_phone.place(x=180, y=250)

insert = Button(root, text="Insert", bg="black",
                fg="white", font=("Arial", 10), command=insertData)
insert.place(x=50, y=300)

search = Button(root, text="Search", bg="black",
                fg="white", font=("Arial", 10), command=searchData)
search.place(x=120, y=300)

update = Button(root, text="Update", bg="black",
                fg="white", font=("Arial", 10), command=updateData)
update.place(x=210, y=300)

delete = Button(root, text="Delete", bg="black",
                fg="white", font=("Arial", 10), command=deleteData)
delete.place(x=290, y=300)

clearEntry = Button(root, text="Clear Entry", bg="black",
                    fg="white", font=("Arial", 10), command=flushEntry)
clearEntry.place(x=50, y=350)
clearEntry.config(width=35)

root.mainloop()
