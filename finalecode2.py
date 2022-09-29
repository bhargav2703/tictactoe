import pygame
import pygame
from pygame.constants import MOUSEBUTTONDOWN
import sys
from random import randint
import finalecode2
from tkinter import *
# import os
sys.stdout = open("sector1.txt","a")
pygame.init()
pygame.HWSURFACE
pygame.SCALED
choice = randint(1,2)
mouseX = 0
mouseY = 0
checker = 99
player = Tk()
player.configure(bg = "black")
player.resizable(False,False)
w = 400
h = 80
ws = player.winfo_screenwidth() 
hs = player.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
player.geometry('%dx%d+%d+%d' % (w, h, x, y))
if(choice == 1):   
    labelpl = Label(player,text = "O starts the game",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack(padx = 10,pady = 13)
if(choice == 2):
    labelpl = Label(player,text = "X starts the game",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack(padx = 10,pady = 13)
# buttclose = Button(player,text = "start game",command = player.destroy).pack()
player.mainloop()
screen = pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption("tictactoe")
icon = pygame.image.load('gamifi.png')
pygame.display.set_icon(icon)
gameboardavail = [[1]*3,[1]*3,[1]*3]
#gameover represents if the game is over
clicknumber = 0
gameover = 0
#cross n nought represent x and o resp
cross = pygame.image.load('closer.png')
nought = pygame.image.load('circle-ringer.png')
player = [[0]*3,[0]*3,[0]*3]
running = True
# a and b resp represent the point where the image is to be dosplayed whic changes frm box to box
a = 1000
b = 1000
winner = 0
def nought_disp(a,b):
    screen.blit(nought,(a,b))
def cross_disp(c,d):
    screen.blit(cross,(c,d))
playernum = 0
#marksquare marks the player who has clicked each box and changes the availability of the box after a click
def marksquare(playernum,row,col):
    player[row-1][col-1] = playernum
    gameboardavail[row-1][col-1] = 0
winnermod = False
#variables for current click and previous click matching
c = 1010
d = 1011
c1 = 100000
d1 = 1832
a1 = 93829
b1 = 99311
screen.fill((255,0,0))
#start the while loop only if the running condition is True it becomes False when the game ends or the close button is clicked
while running == True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False 
            sys.exit()
#draw the grid lines for the tictactoe layout
    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),6)
    pygame.draw.line(screen,(0,0,0),(400,0),(400,600),6)
    pygame.draw.line(screen,(0,0,0),(0,200),(600,200),6)
    pygame.draw.line(screen,(0,0,0),(0,400),(600,400),6)
#display an x or and display based on the player who has clicked
    if (choice == 1):
        if(c1 == c and d1 == d):
            nought_disp(a,b)
        if(a1==a and b1 == b):
          cross_disp(c,d)
    if (choice == 2):
        if(c1 == c and d1 == d):
            cross_disp(a,b)
        if(a1==a and b1 == b):
            nought_disp(c,d)  
#drawing lines if any of the player has won the game
    if(clicknumber>=5):
        if(player[2][2]!=0):    
                if(player[0][0]==player[1][1]==player[2][2]):#L1
                    pygame.draw.line(screen,(255,255,255),(82.33,82.33),(475,475),6)
                    #running  = False
                    winner = player[0][0]
                    winnermod = True
        if(player[0][0]!=0):    
                if(player[0][0]==player[0][1]==player[0][2]):
                    pygame.draw.line(screen,(255,255,255),(102.33,102.33),(503,102.33),6)
                    winner = player[0][0]
                    winnermod = True
        if(player[2][0]!=0):    
                if(player[0][0]==player[1][0]==player[2][0]):
                    pygame.draw.line(screen,(255,255,255),(102.33,102.33),(102.33,503),6)
                    winner = player[0][0]
                    winnermod = True
        if(player[1][0]!=0):    
                if(player[1][0]==player[1][1]==player[1][2]):
                    pygame.draw.line(screen,(255,255,255),(102.33,303),(503,303),6)
                    winner = player[1][0]
                    winnermod = True
        if(player[2][1]!=0):    
                if(player[0][1]==player[1][1]==player[2][1]):
                    pygame.draw.line(screen,(255,255,255),(303,102.33),(303,503),6)
                    winner = player[0][1]
                    winnermod = True
        if(player[2][0]!=0):    
                if(player[0][2]==player[1][1]==player[2][0]):
                    pygame.draw.line(screen,(255,255,255),(503,102.33),(102.3,503),6)
                    winner = player[0][2]
                    winnermod = True 
        if(player[2][2]!=0):
                if(player[0][2]==player[1][2]==player[2][2]):
                    pygame.draw.line(screen,(255,255,255),(503,102.33),(503,503),6)
                    winner = player[2][2]
                    winnermod = True
        if(player[2][2]!=0):    
                if(player[2][0]==player[2][1]==player[2][2]) :
                    pygame.draw.line(screen,(255,255,255),(102.33,503),(503,503),6)
                    winner = player[2][2]
                    winnermod = True      
        if(clicknumber == 9 and winner == 0):
                    gameover=2
#ensuring that the rownum and colnum are updated after every click
    a1 = a
    b1 = b
    c1 = c
    d1 = d
#clickX,clickY represents the point where the mouse is clicked
    pygame.display.update()
    clickX = 0
    clickY = 0
#checking if the mouse was clicked
    if event.type == pygame.MOUSEBUTTONDOWN :

        mouseX = event.pos[0]  #x
        mouseY = event.pos[1]  #y
#ensuring that a click on the lines dont count 
        if(mouseX in range(0,190) or mouseX in range(210,390) or mouseX in range(410,600)):
            if(mouseY in range(0,192) or mouseY in range(198,392) or mouseY in range(398,600)):
                clickX = mouseX//200 + 1
                clickY = mouseY//200 + 1 
        else:
            continue
#checking which box is clicked
        if(gameboardavail[clickY-1][clickX-1] == 1):
            clicknumber = clicknumber + 1
            if(clicknumber == 1):
                playernum = 1
            if(clicknumber > 1):
                if(clicknumber % 2 == 1):
                    playernum = 1
                if(clicknumber % 2 == 0):
                    playernum = 2
            if clickX == 1 and clickY == 1:
                if(playernum == 1):
                    a = 72.33
                    b = 72.33
                if(playernum == 2):
                    c = 72.33
                    d = 72.33
            if clickX == 2 and clickY == 2:
                if(playernum == 1):
                    a = 263
                    b = 263
                if(playernum == 2):
                    c = 265
                    d = 265
            if clickX == 3 and clickY == 3:
                if(playernum == 1):
                    a = 465
                    b = 465
                if(playernum == 2):
                    c = 465
                    d = 465
            if clickX == 1 and clickY == 2:
                if(playernum == 1):
                    a = 72.33
                    b = 265
                if(playernum == 2):
                    c = 72.33
                    d = 265
            if clickX == 1 and clickY == 3:
                if(playernum == 1):
                    a = 72.33
                    b = 465
                if(playernum == 2):
                    c = 72.33
                    d = 465
            if clickX == 2 and clickY == 3:
                if(playernum == 1):
                    a = 265
                    b = 465
                if(playernum == 2):
                    c = 265
                    d = 465
            if clickX == 2 and clickY == 1:
                if(playernum == 1):
                    a = 265
                    b = 72.33
                if(playernum == 2):
                    c = 265
                    d = 72.33
            if clickX == 3 and clickY == 1:
                if(playernum == 1):
                    a = 465
                    b = 72.33
                if(playernum == 2):
                    c = 465
                    d = 72.33
            if clickX == 3 and clickY == 2:
                if(playernum == 1):
                    a = 465
                    b = 265
                if(playernum == 2):
                    c = 465
                    d = 265
            marksquare(playernum,clickY,clickX)
    #check if the winner is the player who started first
    if(clicknumber <= 9 and winner == 1):
            root = Tk()
            root.resizable(False,False)
            root.configure(bg = "black")
            root.geometry("300x100+%d+%d"%(580,380))
            if(choice == 1):
                label = Label(text = "CONGRATULATIONS!!!  O won the game",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2)
            if(choice == 2):
                label = Label(text = "CONGRATULATIONS!!!  X won the game",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2)
            label.pack()
            but1 = Button(text = "play again",command = (root.destroy),justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
            but2 = Button(text = "exit",command = exit,justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
            checker = 91
            running = False
            root.title("game over")
            root.mainloop()
            gameover = 1
    #check if the winner is the player who started first
    if(clicknumber <= 9 and winner == 2  ):
            root = Tk()
            root.resizable(False,False)
            root.configure(bg = "black")
            root.geometry("300x100+%d+%d"%(580,380))
            if(choice ==2 ):
                label = Label(text = "CONGRATULATIONS!!! O has won the game",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2)
            if(choice == 1):
                label = Label(text = "CONGRATULATIONS!!! X has won the game",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2)
            label.pack()
            but1 = Button(text = "play again",command = (root.destroy),justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
            but2 = Button(text = "exit",command = exit,justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
            root.title("game over")
            running = False
            root.mainloop()
            checker = 91
            gameover = 1
            fincheck = 2
            print(clicknumber)
    #check if it is a draw
    if(clicknumber == 9 and winnermod == False):
        if(checker == 99):
            if(gameover == 2):
                root = Tk()
                root.resizable(False,False)
                root.configure(bg = "black")
                root.geometry("300x100+%d+%d"%(580,380))
                lab = Label(root,text = "DRAW !!!",justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
                but1 = Button(text = "play again",command = root.destroy,justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
                but2 = Button(text = "exit",command = exit,justify=CENTER,bg = "black",fg= "red",font = ("Arial",12),border=2).pack()
                root.mainloop()
                running = False
            
print(gameboardavail)
print(player,end = "\n")