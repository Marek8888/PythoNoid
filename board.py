import pygame


class Board:
    def __init__(self, pytho, image_file):
        self.screen = pytho.screen
        self.screen_rect = pytho.screen.get_rect()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        # Set board speed
        self.speed = 1

        self.is_moving_right = False
        self.is_moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_move(self):
        if self.is_moving_right:
            self.x += self.speed
        if self.is_moving_left:
            self.x -= self.speed
        self.rect.x = self.x

