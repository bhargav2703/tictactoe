from tkinter import *
import sys
import os
def hellocallme():
    os.system('finalecode.py')
def hellocallmee():
    os.system('instructions.py')
def hellocallmmee():
    os.system('resources.py')
def hellocalllme():
    os.system('resource.py')
root = Tk()
root.geometry("600x600")
bg = PhotoImage(file="finale.png")
mylab = Label(root,image = bg)
mylab.place(x = 0,y = 0,relwidth= 1,relheight=1)
Labl = Label(text = "TIC-TAC-TOE",justify=CENTER,font = ("Jokerman",35),bg = "black",fg = "red",border = 5).pack(pady = 20)
but1 = Button(text = "Play",command = hellocallme,justify=CENTER,bg = "black",fg= "red",font = ("Arial",18),border=2).pack()
but2  = Button(text = "Help",command = hellocallmee,justify=CENTER,bg = "black",fg = "red",font = ("Arial",18),border = 2).pack(padx = 20,pady = 20)
but3 = Button(text = "Team",command = hellocallmmee,justify=CENTER,bg = "black",fg = "red",font = ("Arial",18),border = 2).pack(padx = 50)
but4 = Button(text = "Resources",command = hellocalllme,justify=CENTER,bg = "black",fg = "red",font = ("Arial",18),border = 2).pack(padx = 50,pady = 20)
root.mainloop() 