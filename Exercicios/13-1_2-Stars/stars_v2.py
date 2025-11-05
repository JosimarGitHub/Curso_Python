import sys
import pygame
import time
from random import randint
from star import Estrela

class Star_Blink:

    def __init__(self):
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1450, 850))
        pygame.display.set_caption("BLINK STARTS")
        self.color = (0, 0, 0)
        
        self.estrelas = pygame.sprite.Group()
        
    
    def _desenhar_estrela(self,position_x, position_y):
        new_estrela = Estrela(self)
        new_estrela.rect.x = position_x
        new_estrela.rect.y = position_y
        self.estrelas.add(new_estrela)
        
    def _eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _atualizar_tela(self):
        self.screen.fill(self.color)
        position_x = randint(0, 1300)
        position_y = randint(0, 750)
        self._desenhar_estrela(position_x, position_y)
        self.estrelas.draw(self.screen)
        pygame.display.flip()
        time.sleep(0.2)
        for estrela in self.estrelas:
            self.estrelas.remove(estrela)

    def run_game(self):
        while True:
            self._atualizar_tela()
            self._eventos()
            self.clock.tick(60)

if __name__ == '__main__':
    star_screen = Star_Blink()
    star_screen.run_game()

        