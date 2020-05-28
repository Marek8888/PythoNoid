import pygame

from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, pytho):
        super().__init__()
        self.screen = pytho.screen
        self.settings = pytho.settings
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 200
        self.y = float(self.rect.y)
        self.ball_direction = 1

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.y += self.ball_direction * self.settings.ball_speed
        self.rect.y = self.y


