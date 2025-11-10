import pygame

class Rocket:
    def __init__(self,game_shooter):
        self.tela = game_shooter.tela
        self.tela_rect = game_shooter.tela.get_rect()
        self.image = pygame.image.load('/home/dev_net/Desktop/Curso_Python/Exercicios/12-6._Sideways_Shooter/rocket.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.midleft = self.tela_rect.midleft
        self.image_y = float(self.image_rect.y)
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_up and (self.image_rect.top > self.tela.get_rect().top):
            self.image_y -= 4
        if self.moving_down and (self.image_rect.bottom < self.tela.get_rect().bottom):
            self.image_y += 4
        
        self.image_rect.y = self.image_y
    
    def blitme(self):
        self.tela.blit(self.image, self.image_rect)