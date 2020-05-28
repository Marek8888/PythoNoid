import pygame


class Board:
    def __init__(self, pytho, image_file):
        self.screen = pytho.screen
        self.screen_rect = pytho.screen.get_rect()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

