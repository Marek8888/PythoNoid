import pygame

import sys

from settings import Settings


class PythoNoid:
    def __init__(self):
        pygame.init()
        # Create a subclass of Settings
        self.settings = Settings(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.screen_color)
            pygame.display.flip()

if __name__ == '__main__':
    game = PythoNoid()
    game.run_game()
