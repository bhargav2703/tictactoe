from tkinter import *
root = Tk()
root.geometry('200x200')
root.title("RESOURCES AND CONTRIBUTORS")
bg = PhotoImage(file="finale.png")
mylab = Label(root,image = bg)
mylab.place(x = 0,y = 0,relwidth= 1,relheight=1) 

Lab2 = Label(text = "contributors - \n Bhargav   \nMohnish   \nPratyush",justify=CENTER,font = ("Arial",12),bg = "black",fg = "red").pack()
root.mainloop()