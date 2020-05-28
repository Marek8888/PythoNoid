import pygame


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen_color = (230,230,230)
        self.ball_speed = 20
        self.clock = pygame.time.Clock()
