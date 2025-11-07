import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, rd_show):

        super().__init__()
        self.screen = rd_show.screen

        self.image = pygame.image.load('chuva.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rain_drop_speed = 1
    
    def check_in_bottom(self):

        return (self.image.get_rect().y > self.screen.get_rect().bottom)
            
    def update(self):

        self.rect.y += self.rain_drop_speed
