import pygame

import sys

from settings import Settings

from board import Board

from ball import Ball


class PythoNoid:
    def __init__(self):
        pygame.init()
        # Create a subclass of Settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Create board sublass
        self.board_sprite = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.board = Board(self)
        self.board_sprite.add(self.board)
        self.ball = Ball(self)
        self.balls.add(self.ball)

    def _check_key_ups(self, event):
        """Check agains key releases"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.board.is_moving_left = False
            if event.key == pygame.K_RIGHT:
                self.board.is_moving_right = False

    def _check_for_key_downs (self,event):
        """Check agains key presses"""
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_LEFT:
                self.board.is_moving_left = True
            if event.key == pygame.K_RIGHT:
                self.board.is_moving_right = True

    def check_events(self):
        """Check for keybord events"""
        for event in pygame.event.get():
            self._check_for_key_downs(event)
            self._check_key_ups(event)

    def _update_ball_direction(self):
        self.ball.direction_y = -1
        self.ball.direction_x = -1

    def check_ball_hit(self):
        if pygame.sprite.groupcollide(self.board_sprite, self.balls, False, False):
            if self.ball.rect.x in self.board.incline_0[0] or self.ball.rect.x in self.board.incline_0[1]:
                self.ball.direction_y = -1
                self.ball.incline = 0
            elif self.ball.rect.x in self.board.incline_medium[0]:
                print ('incline medium left' )
                self.ball.x0 = self.ball.x
                self.ball.incline = -1
            elif self.ball.rect.x in self.board.incline_medium[1]:
                print('incline medium right')
                self.ball.x0 = self.ball.x
                self.ball.incline = 1
            elif self.ball.rect.x in self.board.incline_high[0]:
                print('high left')
                self.ball.x0 = self.ball.rect.x
                self.ball.incline = -2
            elif self.ball.rect.x in self.board.incline_high[1]:
                print('high right')
                self.ball.x0 = self.ball.rect.x
                self.ball.incline = 2
        if self.ball.rect.x <= 0:
            self.ball.x0 = 0
            self.ball.incline = self.ball.incline * (-1)
            print('left wall')

    def run_game(self):
        while True:
            self.check_events()
            self.screen.fill(self.settings.screen_color)
            self.board.blitme()
            self.ball.blitme()
            self.board.update_move()
            self.check_ball_hit()
            #print(self.board.incline_0, self.board.incline_medium, self.board.incline_high)
            print(f" incline:{self.ball.incline}, x:{self.ball.rect.x}, x0:{self.ball.x0}, y:{self.ball.rect.y}")
            pygame.display.flip()
            self.ball.update()
            self.settings.clock.tick(30)


if __name__ == '__main__':
    game = PythoNoid()
    game.run_game()
