#!/usr/bin/env python
"""tictactoe.py

A simple Tic-Tac-Toe game for two players. The Keypad is used.

"Fill" means the area (corresponding to 1-9 on the keypad) is full with something, either an X or an O. X(1-9) and O(1-9) relate to the same thing. 

"""
##Initialization settings
import pygame
from pygame.locals import *
screen_size = 320,320
background = 255,255,255
BLACK=0,0,0

##Screen Initializes
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")
screen.fill(background)

##Draw the lines
pygame.draw.line(screen, (0,0,0),(105,20),(105,300), 10)
pygame.draw.line(screen, (0,0,0),(205,20),(205,300), 10)
pygame.draw.line(screen, (0,0,0),(20,105),(300,105), 10)
pygame.draw.line(screen, (0,0,0),(20,205),(300,205), 10)

##Fill, O, and X values
fill1=False
fill2=False
fill3=False
fill4=False
fill5=False
fill6=False
fill7=False
fill8=False
fill9=False
O1=False
O2=False
O3=False
O4=False
O5=False
O6=False
O7=False
O8=False
O9=False
X1=False
X2=False
X3=False
X4=False
X5=False
X6=False
X7=False
X8=False
X9=False

##Quitting
done=False
turn1=True
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

##Creating O's
    if turn1==True:
        if event.type == KEYDOWN and event.key == K_KP1 and fill1==False:
            pygame.draw.circle(screen, BLACK, (55,255),40,10)
            fill1=True
            O1=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP2 and fill2==False:
            pygame.draw.circle(screen, BLACK, (155,255),40,10)
            fill2=True
            O2=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP3 and fill3==False:
            pygame.draw.circle(screen, BLACK, (255,255),40,10)
            fill3=True
            O3=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP4 and fill4==False:
            pygame.draw.circle(screen, BLACK, (55,155),40,10)
            fill4=True
            O4=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP5 and fill5==False:
            pygame.draw.circle(screen, BLACK, (155,155),40,10)
            fill5=True
            O5=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP6 and fill6==False:
            pygame.draw.circle(screen, BLACK, (255,155),40,10)
            fill6=True
            O6=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP7 and fill7==False:
            pygame.draw.circle(screen, BLACK, (55,55),40,10)
            fill7=True
            O7=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP8 and fill8==False:
            pygame.draw.circle(screen, BLACK, (155,55),40,10)
            fill8=True
            O8=True
            turn1=False
        elif event.type == KEYDOWN and event.key == K_KP9 and fill9==False:
            pygame.draw.circle(screen, BLACK, (255,55),40,10)
            fill9=True
            O9=True
            turn1=False

##Creating X's
    if turn1==False:
        if event.type == KEYDOWN and event.key==K_KP1 and fill1==False:
            pygame.draw.line(screen, BLACK, (20,220),(95,290),10)
            pygame.draw.line(screen, BLACK, (20,290),(95,220),10)
            fill1=True
            X1=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP2 and fill2==False:
            pygame.draw.line(screen, BLACK, (120,220),(195,290),10)
            pygame.draw.line(screen, BLACK, (120,290),(195,220),10)
            fill2=True
            X2=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP3 and fill3==False:
            pygame.draw.line(screen, BLACK, (220,220),(295,290),10)
            pygame.draw.line(screen, BLACK, (220,290),(295,220),10)
            fill3=True
            X3=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP4 and fill4==False:
            pygame.draw.line(screen, BLACK, (20,120),(95,190),10)
            pygame.draw.line(screen, BLACK, (20,190),(95,120),10)
            fill4=True
            X4=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP5 and fill5==False:
            pygame.draw.line(screen, BLACK, (120,120),(195,190),10)
            pygame.draw.line(screen, BLACK, (120,190),(195,120),10)
            fill5=True
            X5=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP6 and fill6==False:
            pygame.draw.line(screen, BLACK, (220,120),(295,190),10)
            pygame.draw.line(screen, BLACK, (220,190),(295,120),10)
            fill6=True
            X6=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP7 and fill7==False:
            pygame.draw.line(screen, BLACK, (20,20),(95,90),10)
            pygame.draw.line(screen, BLACK, (20,90),(95,20),10)
            fill7=True
            X7=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP8 and fill8==False:
            pygame.draw.line(screen, BLACK, (120,20),(195,90),10)
            pygame.draw.line(screen, BLACK, (120,90),(195,20),10)
            fill8=True
            X8=True
            turn1=True
        elif event.type == KEYDOWN and event.key == K_KP9 and fill9==False:
            pygame.draw.line(screen, BLACK, (220,20),(295,90),10)
            pygame.draw.line(screen, BLACK, (220,90),(295,20),10)
            fill9=True
            X9=True
            turn1=True

##O Victory
    if O1==True and O2 == True and O3 == True                                          or O1 == True and O4 == True and O7 == True                                     or O1 == True and O5 == True and O9 == True                                     or O2 == True and O5 == True and O8 == True                                     or O3 == True and O6 == True and O9 == True                                     or O3 == True and O5 == True and O7 == True                                     or O4 == True and O5 == True and O6 == True                                     or O7 == True and O8 == True and O9 == True:
        done=True
        print "O's win!"
        print "Make 'em say OOOOH!"

##X Victory
    if X1==True and X2 == True and X3 == True                                          or X1 == True and X4 == True and X7 == True                                     or X1 == True and X5 == True and X9 == True                                     or X2 == True and X5 == True and X8 == True                                     or X3 == True and X6 == True and X9 == True                                     or X3 == True and X5 == True and X7 == True                                     or X4 == True and X5 == True and X6 == True                                     or X7 == True and X8 == True and X9 == True:
        done=True
        print "X's win!"
        print "I don't always win, but when I do, it's with Tres Equis."

    if fill1 == True and fill2 == True and fill3 == True                                             and fill4 == True and fill5 == True                                             and fill6 == True and fill7 == True                                             and fill8 == True and fill9 == True:
        done=True
        print "Tie game"
        print "This is what happens when an unstoppable force meets and immovable object."


    pygame.display.flip()
