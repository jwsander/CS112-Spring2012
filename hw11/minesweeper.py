#!/usr/bin/ env python

import pygame
import pygame, random
from pygame.locals import *

##Globals

GREY = 80,80,80
WHITE = 150,150,150
RED = 255,0,0
GREEN = 0, 255, 0
BLACK = 0,0,0
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 30
SQ_SIZE = 60,60
gameover = False
win = False
lose = False
end = False

##Functions
#Draw Flag
def drawFlag((x,y)):
    pole = pygame.Rect((x-5,y-20), (5,35))
    pygame.draw.rect(screen, BLACK, pole)
    pygame.draw.polygon(screen, GREEN, [(x,y-20),(x+20,y-10),(x,y)])

#Draw Mine
def drawMine((p,q)):
    bombtop = pygame.Rect((p-8,q-12),(16,5))
    fuse = pygame.Rect((p-2,q-18),(5,10))
    pygame.draw.circle(screen, BLACK, (p,q+5), 15)
    pygame.draw.rect(screen, BLACK, fuse)
    pygame.draw.rect(screen, GREY, bombtop)

#Enlarge Mines
def rectGrower((x1,y1), (x2,y2), (x3,y3), (x4,y4)):
    x1,y1 = x1 - 5, y1 - 5  #Top left
    x2,y2 = x2 + 5, y2 - 5  #Top Right
    x3,y3 = x3 - 5, y3 + 5  #Bottom Left
    x4,y4 = x4 + 5, y4 + 5  #Bottom Right
    x5,y5 = x1, y1 +15      #Left
    x6,y6 = x2, y2 +15      #Right
    x7,y7 = x3 + 15, y3     #Bottom
    x8,y8 = x1 + 15, y1     #Top

    return [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8)]

##Initialize Screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

##Objects
bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 40)
bounds = screen.get_rect()
rects = []
underrects = []
clickedrt = []
mines = []
boompoints = []
safes = []

 #Grid
for a in range(0,600,60):
    for b in range(0,600,60):
        sq = pygame.Rect((a,b),SQ_SIZE)
        rects.append(sq)
        underrects.append(sq)

 #Mines
mines = random.sample(rects,10)
mines = sorted(mines)
for mine in mines:
    pt = rectGrower(mine.topleft,mine.topright,mine.bottomleft,mine.bottomright)
    boompoints.extend(pt)


##Game Loop
clock = pygame.time.Clock()
done = False
while not done:

    ##Input
    for evt in pygame.event.get():
        #Quit
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True

        #Click on rect
        elif evt.type == MOUSEBUTTONDOWN and evt.button == 1:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()) and end == False and rect not in clickedrt:
                    rects.remove(rect)
                    if rect in mines:
                        lose = True

        #Flagging
        elif evt.type == MOUSEBUTTONDOWN and evt.button == 3:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()) and rect in rects  and end == False:
                    if rect not in clickedrt:
                        clickedrt.append(rect)
                    elif rect in clickedrt:
                        clickedrt.remove(rect)

    ##DRAW
    screen.fill(WHITE)

    #Draw background Grid
    for rect in underrects:
        pygame.draw.rect(screen,BLACK,rect,1)

    #Flag
    for rect in clickedrt:
        drawFlag(rect.center)
        clickedrt = sorted(clickedrt)

    #Mine
    for rect in mines:
        if rect not in rects:
            drawMine(rect.center)

    #Numbers
    for rect in underrects:
        if rect not in rects:
            minesNear = 0
            for boompoint in boompoints:
                if rect.collidepoint(boompoint):
                    minesNear += 1
            if minesNear > 0 and rect not in mines:
                text = smallfont.render(str(minesNear), True, (0,0,0),WHITE)
                loc = text.get_rect()
                loc.center = rect.center
                screen.blit(text,loc)

    ##Clearing multiple spaces
            elif minesNear == 0:
                safe = rectGrower(rect.topleft,rect.topright,rect.bottomleft,rect.bottomright)
                safes.extend(safe)
    for rect in rects:
        for safe in safes:
            if rect.collidepoint(safe) and rect in rects:
                rects.remove(rect)
                safes = []

    ##Draw Top Grid
    for rect in rects:
        if rect in mines and end == True:
            color = RED
        else:
            color = GREY
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)
    
    ##Draw Flag
    for rect in clickedrt:
        drawFlag(rect.center)
        clickedrt = sorted(clickedrt)

    if clickedrt == mines:
        win = True
    
    ##Winning
    if win == True:
        end = True
        wintext = bigfont.render("YOU WIN!", True, (0,0,0),GREEN)
        locw = wintext.get_rect()
        locw.center = bounds.center
        screen.blit(wintext,locw)
    
    ##Losing
    if lose == True:
        end = True
        losetext = bigfont.render("YOU LOSE!", True, (0,0,0),GREEN)
        locl = losetext.get_rect()
        locl.center = bounds.center
        screen.blit(losetext,locl)

    #refresh
    pygame.display.flip()
