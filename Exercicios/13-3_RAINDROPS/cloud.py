import pygame
from pygame.sprite import Sprite

class Cloud(Sprite):

    def __init__(self, rd_show):

        super().__init__()
        self.screen = rd_show.screen

        self.image = pygame.image.load('nuvem.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width

        