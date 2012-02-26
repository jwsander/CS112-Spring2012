#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

##Variables
red_x, red_y = 10, 250
red_dx, red_dy = 0,0
blue_x, blue_y = 590, 250
blue_dx, blue_dy = 0, 0
blues = []
reds = []
lines = []
BLUE = (0, 0, 255)
RED = (255, 0, 0)

##Drawing the player cube function
def drawTron(surf, pos, color =(255,255,255), cube=10):
    x,y = pos
    draw.rect(surf, color, (x, y, cube, cube))

##Move function
def move(x, y, dx, dy, up, down, left, right, bounds):
    
    x += dx
    y += dy

    #Up
    if event.type == KEYDOWN and event.key == up and dy != 10:
        dx = 0
        dy = -10 
    #Down
    if event.type == KEYDOWN and event.key == down and dy != -10:
        dx = 0
        dy = 10
    #Left
    if event.type == KEYDOWN and event.key == left and dx != 10:
        dx = -10
        dy = 0
    #Right
    if event.type == KEYDOWN and event.key == right and dx != -10:
        dx = 10
        dy = 0

    #Bounds
    if y < bounds.top or y > bounds.bottom:
        dx, dy = 0, 0
        endGame = True
    if x < bounds.left or x > bounds.right:
        dx, dy = 0,0
        endGame = True
    return x, y, dx, dy

##Initializing Voodoo
pygame.init()
screen = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()


##Quitting
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    screen.fill((0,0,0))

##Starting
    if event.type == KEYDOWN and event.key == K_SPACE and blue_x == 590 and  blue_y == 250 and red_x == 10 and red_y == 250:
        blue_dx, blue_dy = -10, 0
        red_dx, red_dy = 10,0

        
##Drawing Red
    red_x, red_y, red_dx, red_dy = move(red_x, red_y, red_dx, red_dy, K_w, K_s, K_a, K_d, screen_bounds)
    reds.append([red_x,red_y])
    for i in range(len(reds)):
        drawTron(screen, reds[i], RED)

    #Collision Red
    for l in lines:
        if (red_x, red_y) == l:
            red_dx, red_dy = 0, 0
    lines.append((red_x, red_y))


##Drawing Blue
    blue_x, blue_y, blue_dx, blue_dy = move(blue_x, blue_y, blue_dx, blue_dy, K_UP, K_DOWN, K_LEFT, K_RIGHT, screen_bounds)
    blues.append([blue_x,blue_y])
    for u in range (len(blues)):
        drawTron(screen, blues[u], BLUE)

        #Collision Blue
    for l in lines:
        if (blue_x, blue_y) == l:
            blue_dx, blue_dy = 0, 0
    lines.append((blue_x, blue_y))


##Freezing the game
    if blue_dx == 0 and blue_dy == 0:
        red_dx, red_dy = 0, 0
        
    if red_dx == 0 and red_dy == 0:
        blue_dx, blue_dy = 0, 0


    pygame.display.flip()
    clock.tick(60)


