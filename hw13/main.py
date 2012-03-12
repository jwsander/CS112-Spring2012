#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_tie, draw_ywing, draw_bullet, draw_player
from ships import Ship, ShipSpawner
from utils import *


## EXPLOSIONS
class ExplosionGroup(Group):
    def draw(self, surf):
        for xplo in self:
            if xplo.radius > 0:
                xplo.draw(surf)

class Explosion(Sprite):
    dradius = 60
    duration = 1500
    group = ExplosionGroup()

    def __init__(self, pos, radius):
        Sprite.__init__(self)
        self.pos = pos
        self.radius = radius

    def update(self, dt):
        if self.duration > 0:
            self.duration -= dt
        elif self.radius > 0:
            self.radius -= self.dradius * (dt / 1000.0)
        else:
            self.kill()

    def rand_color(self):
        return randrange(120,256), 255, randrange(120,256)

    def draw(self, surf):
        pygame.draw.circle(surf, self.rand_color(), self.pos, int(self.radius))



class Explodes(Sprite):
    explosion_type = Explosion
    explosion_radius = 60

    def kill(self):
        xplo = self.explosion_type(self.rect.center, self.explosion_radius)
        Explosion.group.add(xplo)
        Sprite.kill(self)


def collide_xplo_ship(xplo, ship):
    return collide_rect_circle(ship.rect, xplo.pos, xplo.radius)

## SHIP GROUP
class ShipGroup(Group):
    def __init__(self, count):
        Group.__init__(self)
        self.count = count

    def add(self, *sprites):
        for sprite in sprites:
            if len(self) < self.count:
                Group.add(self, sprite)

##Player
class Player(Ship):
    width = 40
    height = 40
    def __init__(self, x, y, vx, vy, bounds, color):
        Sprite.__init__(self)

        self.vx = vx
        self.vy = vy
        self.bounds = bounds
        self.color = color

        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()
        

    def draw_image(self):
        draw_player(self.image, self.color)

    def update(self, dt):
        vx = 0
        vy = 0

    def move(self, dir):
        if dir=="w":
            self.rect.y -= self.vy
        if dir=="s":
            self.rect.y += self.vy
        if dir=="a":
            self.rect.x -= self.vx
        if dir=="d":
            self.rect.x += self.vx




#        dx = int(self.vx)
#        dy = int(self.vy)
#        self.rect.x += dx
#        self.rect.y += dy

#        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
#            self.vx = -self.vx
#            self.rect.x += -2 * dx

#        if self.rect.top < self.bounds.top or if self.rect.top > self.bounds.bottom:
#            self.vy = -self.vy
#            self.rect.y += -2 * dy


class PlayerSpawner(ShipSpawner):
    ship_type = Player

    def rand_vel(self):
        vx = 0
        vy = 500
        return vx, vy

    def rand_color(self):
        r = randrange(128,172)
        return r,r,r

    def spawn(self):
        x = self.bounds.width/2
        y = self.bounds.bottom-40
        vx, vy = self.rand_vel()
        color = self.rand_color()

        ship = self.ship_type(x, y, vx, vy, self.bounds, color)
        self.group.add(ship)


##BULLETS

class Bullet(Ship):
    width = 10
    height = 10

    
    def draw_image(self):
        draw_bullet(self.image, self.color)

    def update(self, dt):
        vx = self.vx
        vy = self.vy

###
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.x += -2 * dx

        if self.rect.top < self.bounds.top:
            Sprite.kill(self)
        if self.rect.top > self.bounds.bottom:
            self.vy = -self.vy
            self.rect.y += -2 * dy
###

        if vx != self.vx or vy != self.vy:
            if vx != self.vx:
                vx = self.vx
                vy = -vy
            else:
                vx = -vx
                vy = self.vy


class BulletSpawner(ShipSpawner):
    ship_type = Bullet

    def __init__(self, duration, group, bounds,player):
        self.group = group
        self.bounds = bounds
        self.duration = duration
        self.time = duration
        self.player = player
        
    def rand_vel(self):
        vx = 0
        vy = 500
        return vx, -vy

    def rand_color(self):
        r = randrange(128,172)
        return r,r,r

    def spawn(self):
        x = self.player.rect.x
        y = self.player.rect.y
        vx, vy = self.rand_vel()
        color = self.rand_color()

        ship = self.ship_type(x, y, vx, vy, self.bounds, color)
        self.group.add(ship)


## TIE FIGHTERS
class TieExplosion(Explosion):
    def rand_color(self):
        r = randrange(256)
        return 255, r, 0

class TieFighter(Explodes, Ship):
    width = 40
    height = 40

    explosion_type = TieExplosion
    explosion_radius = 28

    def draw_image(self):
        draw_tie(self.image, self.color)

    def update(self, dt):
        vx = self.vx
        vy = self.vy

        Ship.update(self, dt)

        if vx != self.vx or vy != self.vy:
            if vx != self.vx:
                vx = self.vx
                vy = -vy
            else:
                vx = -vx
                vy = self.vy


class TieSpawner(ShipSpawner):
    ship_type = TieFighter

    def rand_vel(self):
        vx = 0
        vy = randint_neg(200, 250)
        return vx, vy

    def rand_color(self):
        r = randrange(128,256)
        return r,0,0


## Y-Wing
class YWingExplosion(Explosion):
    def rand_color(self):
        r = randrange(256)
        return r, 255, 255

class YWing(Explodes, Ship):
    width = 128
    height = 64

    explosion_type = YWingExplosion

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
        vy = -100
        vx = randint_neg(200, 400)
        return vx, vy

    def rand_color(self):
        r = randrange(128,256)
        return r,r,r

## GAME
class Game(Application):
    title = "SMUP"
    screen_size = 800, 600
    min_dt = 200
    max_ships = 600
    pygame.font.init()


    def __init__(self):
        Application.__init__(self)

        self.bounds = self.screen.get_rect()
        self.ships = ShipGroup(self.max_ships)
        self.bullets = ShipGroup(self.max_ships)
        self.xplos = ExplosionGroup()
        self.score = 0
        self.player = Player(400, 560, 20, 20, self.bounds, (255,255,255))
        Explosion.group = self.xplos

        self.spawners = [ TieSpawner(1000, self.ships, self.bounds),
                          YWingSpawner(2000, self.ships, self.bounds) ]

        

    def handle_event(self, event):

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.xplos.add( Explosion(pygame.mouse.get_pos(), 30) )

        elif event.type == KEYDOWN and event.key == K_f:
            dt = min(self.min_dt, self.clock.get_time())
            BulletSpawner(500, self.bullets, self.bounds,self.player).update(dt)
        
        elif event.type == KEYDOWN and event.key == K_w:
            self.player.move("w")
        elif event.type == KEYDOWN and event.key == K_s:
            self.player.move("s")
        elif event.type == KEYDOWN and event.key == K_a:
            self.player.move("a")
        elif event.type == KEYDOWN and event.key == K_d:
            self.player.move("d")

    def update(self):
        dt = min(self.min_dt, self.clock.get_time())
        self.ships.update(dt)
        self.xplos.update(dt)
        self.bullets.update(dt)

        for xplo in self.xplos:
            pygame.sprite.spritecollide(xplo, self.ships, True, collide_xplo_ship)

        for bullet in self.bullets:
            for ship in self.ships:
                if pygame.sprite.collide_rect(bullet, ship):
                    ship.kill()
                    Sprite.kill(bullet)
                    self.score +=1


        for spawner in self.spawners:
            spawner.update(dt)

    def draw(self, screen):
        smallfont = pygame.font.Font(None,80)
        screen.fill((0,0,0))
        text = smallfont.render(str(self.score), True,(255,255,255), (0,0,0))
        loc = text.get_rect()
        loc.center = self.bounds.center
        screen.blit(text,loc)

        self.ships.draw(screen)
        self.xplos.draw(screen)
        self.bullets.draw(screen)
        self.player.draw_image()
        pygame.draw.circle(screen, self.player.color,(self.player.rect.x,self.player.rect.y),10)
        

if __name__ == "__main__":
    Game().run()
    print "ByeBye"
