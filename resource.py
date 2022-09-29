from tkinter import *
root = Tk()
root.geometry('200x200')
root.title("RESOURCES AND CONTRIBUTORS")
bg = PhotoImage(file="finale.png")
mylab = Label(root,image = bg)
mylab.place(x = 0,y = 0,relwidth= 1,relheight=1) 
Lab1 = Label(text = "Technology Used -\n\n\n -tkinter(8.6)\n -pygame(2.1.0) \n -sys and os modules \n -python(3.9.2)",justify=CENTER,font = ("Arial",12),bg = "black",fg = "red").pack()
root.mainloop()