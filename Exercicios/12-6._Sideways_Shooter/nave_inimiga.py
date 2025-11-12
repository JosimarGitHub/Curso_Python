import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Cria uma classe da nave inimiga"""

    def __init__(self, game_shooter):

        super().__init__()
        self.tela = game_shooter.tela
        self.tela_rect = game_shooter.tela.get_rect()
        self.image = pygame.image.load('/home/dev_net/Desktop/Curso_Python/Exercicios/12-6._Sideways_Shooter/nave.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.direction = 0
        self.velocidade_frota = game_shooter.velocidade
    
    def update(self):

        self.x = float(self.rect.x)
        self.x -= self.velocidade_frota
        self.rect.x = self.x

    def deteccao_fim_tela(self):
        
        if self.rect.top <= 0:
            self.direction = 1
            return self.direction
        if self.rect.bottom >= self.tela.get_rect().bottom:
            self.direction = -1
            return self.direction
