import pygame
from pygame.constants import MOUSEBUTTONDOWN
import sys
import timeit
from tkinter import *
sys.stdout = open("sector1.txt","a")
root = Tk()
root.title("game over")
root.geometry("300x50")
pygame.init()
pygame.HWSURFACE
pygame.SCALED
#screen size is of form width,height
screen = pygame.display.set_mode((600,600),0,32)

#FPS = 10
mouseX = 0
mouseY = 0

pygame.display.set_caption("tictactoe")
icon = pygame.image.load('gamification (1).png')
pygame.display.set_icon(icon)
#gameboard
# 1 - available , 0 - not available
gameboardavail = [[1]*3,[1]*3,[1]*3]
print("gameboard initial availability :",gameboardavail,end='\n ')

#counter
clicknumber = 0
#cross,nough images
cross = pygame.image.load('closer.png')
nought = pygame.image.load('circle-ringer.png')

#player board 0- not player , 1 - player1 , 2- player2
player = [[0]*3,[0]*3,[0]*3]

running = True
a = 1000
b = 1000

winner = 0
def nought_disp(a,b):
    screen.blit(nought,(a,b))
def cross_disp(c,d):
    screen.blit(cross,(c,d))
playernum = 0
print(timeit. timeit())
def marksquare(playernum,row,col):
    #print("row = ",row)
    #print("col = ",col)
    player[row-1][col-1] = playernum
    gameboardavail[row-1][col-1] = 0

c = 1010
d = 1011
c1 = 100000
d1 = 1832
a1 = 93829
b1 = 99311
print("----------------------------------------------------------------------")
screen.fill((255,0,0))
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False 
               #screen.fill((255,255,255))
    #print("in while loop")

    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),6)
    pygame.draw.line(screen,(0,0,0),(400,0),(400,600),6)
    pygame.draw.line(screen,(0,0,0),(0,200),(600,200),6)
    pygame.draw.line(screen,(0,0,0),(0,400),(600,400),6)
    if(c1 == c and d1 == d):
        nought_disp(a,b)
    if(a1==a and b1 == b):
      cross_disp(c,d)
    if(clicknumber==9):
        if(winner ==0):
            label = Label(text = "WELL PLAYED!!! IT's A DRAW")
            label.pack()
            running = False
            clicknumber = 10
            #root.mainloop()
    if(clicknumber>=5):
        if(player[2][2]!=0):    
            if(player[0][0]==player[1][1]==player[2][2]):#L1
                print('L1')
                pygame.draw.line(screen,(255,255,255),(82.33,82.33),(475,475),6)
                #running  = False
                winner = player[0][0]
        if(player[0][0]!=0):    
            if(player[0][0]==player[0][1]==player[0][2]):
                print('L2')
                pygame.draw.line(screen,(255,255,255),(102.33,102.33),(503,102.33),6)
                #running  = False
                winner = player[0][0]
            #print("you've won player",player[0][0])
        if(player[2][0]!=0):    
            if(player[0][0]==player[1][0]==player[2][0]):
                print('L3')
                pygame.draw.line(screen,(255,255,255),(102.33,102.33),(102.33,503),6)
           # running  = False
                winner = player[0][0]
            #print("you've won player",player[0][0])
        if(player[1][0]!=0):    
            if(player[1][0]==player[1][1]==player[1][2]):
                print('L4')
                pygame.draw.line(screen,(255,255,255),(102.33,303),(503,303),6)
                winner = player[1][0]
            #running  = False
            #print("you've won player",player[0][0])
        if(player[2][1]!=0):    
            if(player[0][1]==player[1][1]==player[2][1]):
                print('L5')
                pygame.draw.line(screen,(255,255,255),(303,102.33),(303,503),6)
                winner = player[0][1]
            #running  = False
            #print("you've won player",player[0][0])
        if(player[2][0]!=0):    
            if(player[0][2]==player[1][1]==player[2][0]):
                print('L6')
                pygame.draw.line(screen,(255,255,255),(503,102.33),(102.3,503),6)
                winner = player[0][2]  
        if(player[2][2]!=0):
            if(player[0][2]==player[1][2]==player[2][2]):
                print('L7')
                pygame.draw.line(screen,(255,255,255),(503,102.33),(503,503),6)
                winner = player[2][2]
        if(player[2][2]!=0):    
              if(player[2][0]==player[2][1]==player[2][2]) :
                print('L8')
                pygame.draw.line(screen,(255,255,255),(102.33,503),(503,503),6)
                winner = player[2][2]
        
        else:
            if(clicknumber == 9):
                print("inside else and clicknumber = ",clicknumber)
                print("its a draw")
    a1 = a
    b1 = b
    c1 = c
    d1 = d
    pygame.display.update()
   # print("clicknumber = ",clicknumber)
    # mouse click condition
    clickX = 0
    clickY = 0
    if event.type == pygame.MOUSEBUTTONDOWN :

        mouseX = event.pos[0]  #x
        mouseY = event.pos[1]  #y
        if(mouseX in range(0,190) or mouseX in range(210,390) or mouseX in range(410,600)):
            if(mouseY in range(0,192) or mouseY in range(198,392) or mouseY in range(398,600)):
                clickX = mouseX//200 + 1
                clickY = mouseY//200 + 1 
        else:
            continue
        if(gameboardavail[clickY-1][clickX-1] == 1):
            #change made
            print("row = ",clickX,"columb = ",clickY)
            clicknumber = clicknumber + 1
            print("clicknumber inside the avail condition  - ",clicknumber)
            if(clicknumber == 1):
                playernum = 1
           # print("clicknumber = ",clicknumber)
           #trial only
           # if(clicknumber == 2):
           #    playernum = 2
            if(clicknumber > 1):
                #print(clicknumber)
                if(clicknumber % 2 == 1):
                    playernum = 1
                    print("player num when clicknum is ",clicknumber ,"is",playernum)
                if(clicknumber % 2 == 0):
                    playernum = 2
                    print("player num when clicknum is ",clicknumber ,"is",playernum)


            marksquare(playernum,clickY,clickX)
            #if(clickX == 1 and clickY == 1):
             ##  print("calleddjfliwejfoijijiqfnnqndwiqnwidnewdn")
            if clickX == 1 and clickY == 1:
                if(playernum == 1):
                    a = 72.33
                    b = 72.33
                    print("clicked 1,1 box")
                if(playernum == 2):
                    c = 72.33
                    d = 72.33
                    print("clicked 1,1 box")
            if clickX == 2 and clickY == 2:
                if(playernum == 1):
                    a = 263
                    b = 263
                    print("clicked 2,2 box")
                if(playernum == 2):
                    c = 265
                    d = 265
                    print("clicked 2,2 box")
            if clickX == 3 and clickY == 3:
                if(playernum == 1):
                    a = 465
                    b = 465
                    print("clicked 3,3 box")
                if(playernum == 2):
                    c = 465
                    d = 465
                    print("clicked 3,3 box")
            if clickX == 1 and clickY == 2:
                if(playernum == 1):
                    a = 72.33
                    b = 265
                    print("clicked 1,2 box")
                if(playernum == 2):
                    c = 72.33
                    d = 265
                    print("clicked 1,2 box")
            if clickX == 1 and clickY == 3:
                if(playernum == 1):
                    a = 72.33
                    b = 465
                    print("clicked 1,3 box")
                if(playernum == 2):
                    c = 72.33
                    d = 465
                    print("clicked 1,3 box")
            if clickX == 2 and clickY == 3:
                if(playernum == 1):
                    a = 265
                    b = 465
                    print("clicked 2,3 box")
                if(playernum == 2):
                    c = 265
                    d = 465
                    print("clicked 2,3 box")
            if clickX == 2 and clickY == 1:
                if(playernum == 1):
                    a = 265
                    b = 72.33
                    print("clicked 2,1 box")
                if(playernum == 2):
                    c = 265
                    d = 72.33
                    print("clicked 2,1 box")
            if clickX == 3 and clickY == 1:
                if(playernum == 1):
                    a = 465
                    b = 72.33
                    print("clicked 3,1 box")
                if(playernum == 2):
                    c = 465
                    d = 72.33
                    print("clicked 1,1 box")
            if clickX == 3 and clickY == 2:
                if(playernum == 1):

                    a = 465
                    b = 265
                    print("clicked 3,2 box")
                if(playernum == 2):
                    c = 465
                    d = 265
                    print("clicked 3,2 box")

    if (winner == 1 or winner == 2):
        
    #if(winner == 1 or winner ==2 or winner == 0 ):
        #root.title("game over")
        if(winner == 1):
            label = Label(text = "CONGRATULATIONS!!!PLAYER 1")
            label.pack()
            running = False
        if(winner == 2):
            label = Label(text = "CONGRATULATIONS!!!PLAYER 2")
            label.pack()
            running = False
        root.mainloop()
     #   if(clicknumber == 9):
   
        #var = player[0][0]
        #labe = Label(textvariable=var)
        #labe.pack()
        #text = Entry(root, textvariable = var)
        #text.pack()
        #root.mainloop()
       # if(clicknumber ==9):
        #    clicknumber = 1
    if(clicknumber == 10):
        root.mainloop()
print(gameboardavail)
print(player,end = "\n")
