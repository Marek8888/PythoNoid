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

        # Create board sublasses
        self.board_main = Board(self, 'images/board_middle.bmp')
        self.board_middle_left = Board(self, 'images/board_middleplus.bmp')
        self.board_middle_right = Board(self, 'images/board_middleplus.bmp')
        self.board_side_left = Board(self, 'images/board_side.bmp')
        self.board_side_right = Board(self, 'images/board_side.bmp')
        # update boards posions

    def _print_all_boards(self):
        """Print all boards at they initial positions"""
        self.board_main.blitme()
        self.board_middle_left.blitme()
        self.board_middle_right.blitme()
        self.board_side_left.blitme()
        self.board_side_right.blitme()

        self.board_side_left.rect.midright = self.board_middle_left.rect.midleft
        self.board_middle_left.rect.midright = self.board_main.rect.midleft
        self.board_main.rect.midright = self.board_middle_right.rect.midleft
        self.board_middle_right.rect.midright = self.board_side_right.rect.midleft


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.screen_color)
            self._print_all_boards()
            pygame.display.flip()

if __name__ == '__main__':
    game = PythoNoid()
    game.run_game()
