import pygame
from pygame.sprite import Sprite

class Estrela(Sprite):

    def __init__(self, stars_screen):

        super().__init__()
        self.screen = stars_screen.screen
        self.image = pygame.image.load('estrela_1.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)