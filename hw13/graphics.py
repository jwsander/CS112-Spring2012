#!/usr/bin/env python

import pygame

def colorkey(color):
    if color == (0,0,0):
        return (255,255,255)
    else:
        return (0,0,0)

def clear(surf, color):
    ck = colorkey(color)
    surf.fill(ck)
    surf.set_colorkey(ck)


def draw_tie(surf, color):
    clear(surf, color)
    rect = surf.get_rect()

    d = min(rect.width, rect.height)
    wall = d/8

    dw = rect.width - d
    dh = rect.height - d
    
    pygame.draw.circle(surf, (255,255,255), ( (d+dw)/2, (d+dh)/2 ), d/2)
    pygame.draw.circle(surf,(0,0,0), ((d+dw)/2, (d+dh)/2 + 3), d/5)
    pygame.draw.circle(surf,color, ((d+dw)/2, (d+dh)/2 + 3), d/4, 4)
    

def draw_ywing(surf, color):
    clear(surf, color)
    rect = surf.get_rect()
    
    d = min(rect.width, rect.height)
    
    pygame.draw.circle(surf,color, rect.center, 40)
    pygame.draw.circle(surf, (0,0,0), (d - 5, d), d/2)
    pygame.draw.circle(surf, (255,0,0), (d,d-1),d/6)
    

def draw_bullet(surf, color):
    clear(surf, color)
    rect = surf.get_rect()

    d = min(rect.width, rect.height)
    dw = rect.width - d
    dh = rect.height - d

    pygame.draw.circle(surf, color, ( (d+dw)/2, (d+dh)/2 ), d / 4)
    
def draw_player(surf, color):
    clear(surf, color)
    rect = surf.get_rect()

    d = min(rect.width, rect.height)
    wall = d/8

    dw = rect.width - d
    dh = rect.height - d

    pygame.draw.rect(surf, color, (0, (rect.height - wall)/2, rect.width, wall))

