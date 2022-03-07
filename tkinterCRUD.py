from cProfile import label
from cgi import test
from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("400x400")

l_id = label(root, test="ID")
l_id.place()

root.mainloop()
