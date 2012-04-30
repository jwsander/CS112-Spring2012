"""
game.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import spritecollide, GroupSingle
from app import ApplicationState
from level import Level

class MainMenu(ApplicationState):
    fg_color = 255, 255, 255
    bg_color = 0, 0,0
    flash_rate = 500

    def setup(self):
        pass
        #Put in font

class Game(ApplicationState):
    fps = 60

    def setup(self):
        self.level = Level(self.app.screen.get_size())
        self.level.restart()

    def resume(self):
        self.clock = pygame.time.Clock()
        pygame.mixer.music.unpause()

    def quit(self):
        self.done = True

    def update(self):
        dt = self.clock.tick(self.fps)
        self.level.update(dt)

    def draw(self, screen):
        self.level.draw(screen)

