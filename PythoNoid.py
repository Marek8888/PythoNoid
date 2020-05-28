import pygame

import sys

class PythoNoid:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    game = PythoNoid()
    game.run_game()