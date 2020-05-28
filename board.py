import pygame

from pygame.sprite import Sprite


class Board(Sprite):
    def __init__(self, pytho):
        super().__init__()
        self.screen = pytho.screen
        self.screen_rect = pytho.screen.get_rect()
        self.image = pygame.image.load('images/board.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        # Set board speed
        self.speed = 20
        self.incline_0 = range(0,0)
        self.incline_high = range(0,0)

        self.is_moving_right = False
        self.is_moving_left = False

    def blitme(self):
        """Prints board at the display"""
        self.screen.blit(self.image, self.rect)

    def update_move(self):
        """Update game board movement"""
        if self.is_moving_right:
            self.x += self.speed
        if self.is_moving_left:
            self.x -= self.speed
        self.rect.x = self.x

        # Determine different incline zone depends on where ball hit the board
        self.incline_0 = range(self.rect.centerx - 15, self.rect.centerx + 15)
        self.incline_high = [range(self.rect.left, self.rect.left + 10),
                             range(self.rect.right - 10, self.rect.right)]

