from tkinter import *
root = Tk()
root.geometry("1000x800")
root.title("HOW TO PLAY :)")
bg = PhotoImage(file="unu1.png")
lab1 = Label(text = "HOW TO PLAY").pack()
lab2 = Label(text = "In order to win the game, one of the below eight patterns has to obtained by either player1 and player2 which can be either 'X' or 'O'\n and in an attempt to win the game there might be situations \nwherein no player has won the game and hence its a DRAW",font = ("Arial",12)).pack()
mylab = Label(root,image = bg).pack()

root.mainloop()
