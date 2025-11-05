import sys
import pygame
from star import Estrela

class Star_Blink:

    def __init__(self):
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1450, 850))
        pygame.display.set_caption("BLINK STARTS")
        self.color = (0, 0, 0)
        
        self.estrelas = pygame.sprite.Group()
        self._desenhar_estrela()
    
    def _desenhar_estrela(self):
        estrela = Estrela(self)
        estrela_width, estrela_height = estrela.rect.size
        current_x, current_y = estrela_width, estrela_height

        while current_y < (self.screen.get_rect().height - (2 * estrela_height)):
            while current_x < (self.screen.get_rect().width - (2 *estrela_width)):
                new_estrela = Estrela(self)
                new_estrela.x = current_x
                new_estrela.rect.x = current_x
                new_estrela.rect.y = current_y
                self.estrelas.add(new_estrela)
                current_x += 2 * estrela_width
            current_x = estrela_width
            current_y += 2 * estrela_height

    def _eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _atualizar_tela(self):
        self.screen.fill(self.color)
        self.estrelas.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._atualizar_tela()
            self._eventos()
            self.clock.tick(60)

if __name__ == '__main__':
    star_screen = Star_Blink()
    star_screen.run_game()

        