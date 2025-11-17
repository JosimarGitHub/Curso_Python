import pygame
from pygame.sprite import Sprite

class Missil(Sprite):

    def __init__(self, game_shooter):
        super().__init__()
        self.tela = game_shooter.tela
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, 15, 5)
        self.rect.midleft = game_shooter.rocket.image_rect.midleft
        self.x = float(self.rect.x)

    def update(self):
        self.x += 6
        self.rect.x = self.x

    def draw_missel(self):
        pygame.draw.rect(self.tela, self.color, self.rect)