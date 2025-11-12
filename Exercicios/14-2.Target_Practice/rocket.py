import pygame

class Rocket:
    def __init__(self,game_shooter):
        self.tela = game_shooter.tela
        self.tela_rect = game_shooter.tela.get_rect()
        self.image = pygame.image.load('/home/dev_net/Desktop/Curso_Python/Exercicios/14-2.Target_Practice/rocket.bmp')
        self.image_rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.image_rect.midleft = self.tela_rect.midleft
        self.image_y = float(self.image_rect.y)
        self.moving = False
       
    
    def update(self):
        if self.moving and ((self.image_rect.top > self.tela.get_rect().top) or (self.image_rect.bottom < self.tela.get_rect().bottom)):
            self.image_rect.y = self.image_y
            self.moving = False
    
    def reposition(self):

        self.image_rect.midleft = self.tela_rect.midleft
        self.image_y = float(self.image_rect.y)
    
    def blitme(self):
        self.tela.blit(self.image, self.image_rect)