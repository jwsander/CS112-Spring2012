"""
app.py

"""
import inspect
import pygame
from pygame.locals import *
from pygame.sprite import spritecollide, GroupSingle

from level import Level

class Application(object):
    def __init__(self, state):
        self.screen = pygame.display.get_surface()
        self.set_state(state)

    def quit(self):
        self.done = True
    def set_state(self, state):
        if inspect.isclass(state):
            state = state(self)
            state.resume()
            self.state = state
        
    def run(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                else:
                    self.state.handle_event(event)
            self.state.update()
            self.state.draw(self.screen)
            pygame.display.flip()
            

class ApplicationState(object):
    def __init__(self, app):
        self.app = app
        self.setup()

    def setup(self):
        pass
    def resume(self):
        pass
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, screen):
        pass

class Game(object):
    fps = 60

    def __init__(self, screen):
        self.screen = screen
        self.level = Level(self.screen.get_size())

    def quit(self):
        self.done = True


    def update(self):
        dt = self.clock.tick(self.fps)
        self.level.update(dt)

    def draw(self):
        self.level.draw(self.screen)


    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.level.restart()

        while not self.done:
            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.quit()

            self.update()
            self.draw()
            pygame.display.flip()

