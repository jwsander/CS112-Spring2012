#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_tie, draw_ywing
from ships import Ship, ShipSpawner
from utils import *

## SHIP GROUP
class ShipGroup(Group):
    def __init__(self, count):
        Group.__init__(self)
        self.count = count

    def add(self, *sprites):
        for sprite in sprites:
            if len(self) < self.count:
                Group.add(self,sprite)

##EXPLOSIONS
class Explosion(Sprite):
    dradius = 60
    duration = 1500

    def __init__(self, pos, radius):
        Sprite.__init__(self)
        self.pos = pos
        self.radius = radius

    def update(self,dt):
        if self.duration > 0:
            self.duration -=dt
        elif self.radius > 0:
            self.radius -= self.dradius * (dt / 1000.0)
        else:
            self.kill()

    def rand_color(self):
        return randrange(120,256),255,randrange(120,256)

    def draw(self,surf):
        pygame.draw.circle(surf) ##Update this
##Tie Fighters
class TieFighter(Ship):
    width = 40
    height = 40

    def draw_image(self):
        draw_tie(self.image, self.color)

    def update(self, dt):
        vx = self.vx
        vy = self.vy

        Ship.update(self,dt)

        if vx != self.vx or vy != self.vy:
            if vx != self.vx:
                vx = self.vx
                vy = -vy
            else:
                vx = -vx
                vy = self.vy

            tie = TieFighter(self.rect.x, self.rect.y, vx, vy, self.bounds, self.color)
            for group in self.groups():
                group.add(tie)
        

class TieSpawner(ShipSpawner):
    ship_type = TieFighter

    def rand_vel(self):
        vx = randint_neg(100,250)
        vy = randint_neg(100,250)
        return vx, vy

    def rand_color(self):
        r = randrange(128, 256)
        return r, 0, 0

class YWing(Ship):
    width = 128
    height = 64

    def draw_image(self):
        draw_ywing(self.image, self.color)
        self.orig_image = self.image
        self.flipped_image = pygame.transform.flip(self.image, True, False)

    def update(self, dt):
        if randrange(60) == 0:
            self.vx = -self.vx

        Ship.update(self, dt)
        
        if self.vx > 0:
            self.image = self.orig_image
        else:
            self.image = self.flipped_image

class YWingSpawner(ShipSpawner):
    ship_type = YWing

    def rand_vel(self):
        vx = randint_neg(200,400)
        return vx, 0

    def rand_color(self):
        r = randrange(128, 256)
        return r, r, r



class Game(Application):
    title = "Spaceships"
    screen_size = 800, 600
    min_dt = 200
    max_ships = 600

    def __init__(self):
        Application.__init__(self)

        self.bounds = self.screen.get_rect()
        self.ships = ShipGroup(self.max_ships)

        self.spawners = [ TieSpawner(2000, self.ships, self.bounds),
                          YWingSpawner(2000, self.ships, self.bounds)]

    def update(self):
        dt =  min(self.min_dt, self.clock.get_time())
        
        self.ships.update(dt)

        for spawner in self.spawners:
            spawner.update(dt)

    def draw(self, screen):
        screen.fill((0,0,0))
        self.ships.draw(screen)


if __name__ == "__main__":
    Game().run()
    print "ByeBye"
