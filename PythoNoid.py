import pygame

import sys

from settings import Settings

from board import   Board

class PythoNoid:
    def __init__(self):
        pygame.init()
        # Create a subclass of Settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Create board sublass
        self.board = Board(self, 'images/board.bmp')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.board.is_moving_left = True
            self.screen.fill(self.settings.screen_color)
            self.board.blitme()
            self.board.update_move()
            pygame.display.flip()


if __name__ == '__main__':
    game = PythoNoid()
    game.run_game()
