import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, rd_show):

        super().__init__()
        self.screen = rd_show.screen

        self.image = pygame.image.load('/home/dev_net/Desktop/Curso_Python/Exercicios/13-3_RAINDROPS/chuva.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rain_drop_speed = 1
        
    def update(self):

        self.rect.y += self.rain_drop_speed
