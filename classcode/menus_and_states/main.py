import pygame

from app import Application

from game import Game

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 600))

    app = Application(Game)

    try:
        app.run()
    except KeyboardInterrupt:
        app.quit()
    screen = pygame.display.set_mode((800, 800))

    # create game
    game = Game(screen)
    try:
        game.run()
    except KeyboardInterrupt:
        game.quit()

if __name__ == "__main__":
    main()
