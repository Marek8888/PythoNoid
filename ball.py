import pygame

from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, pytho):
        super().__init__()
        self.screen = pytho.screen
        self.settings = pytho.settings
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 200
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.direction_x = 1
        self.direction_y = 1
        self.x0 = 0
        self.incline = 0

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.incline == 0:
            # Define ball's movement after central part of the board is hit
            self.y += self.direction_y * self.settings.ball_speed
            self.rect.y = self.y
        if self.incline == 1:
            # Define ball movement after right medium part of the board is hit
            self.y = self.settings.screen_height - 23*2 - self.x + self.x0
            self.x += self.settings.ball_speed
            self.rect.y = self.y
            self.rect.x = self.x
        if self.incline == -1:
            # Define ball movement after left medium part of the board is hit
            self.y = self.settings.screen_height - 23 * 2 + self.x - self.x0
            self.x -= self.settings.ball_speed
            self.rect.y = self.y
            self.rect.x = self.x
        if self.incline == 2:
            # Define ball's movement after high right part of the board is hit
            self.y = self.settings.screen_height - 23 * 2 - self.x*0.5 + self.x0*0.5
            self.x += self.settings.ball_speed
            self.rect.y = self.y
            self.rect.x = self.x
        if self.incline == -2:
            # Define ball's movement after high left part of the board is hit
            # high
            self.y = self.settings.screen_height - 23 * 2 + self.x*0.5 - self.x0*0.5
            self.x -= self.settings.ball_speed
            self.rect.y = self.y
            self.rect.x = self.x