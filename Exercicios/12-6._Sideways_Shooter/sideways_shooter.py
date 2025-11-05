import sys
import pygame
from rocket import Rocket
from missil import Missil

class Shooter:
    """ Cria um foguete no canto esquerdo/Centro da Tela
    Que atira missel na vertical"""


    def __init__(self):
        """Iniciando a classe Foguete"""
        #Incio do modulo pygame
        pygame.init()

        #Criando a variavel clock, determina a taxa atualização fps da tela
        self.clock = pygame.time.Clock()

        #Cria uma tela na Resolução desejada
        self.tela = pygame.display.set_mode((1200, 800))

        #Coloca um titulo na Tela criada
        pygame.display.set_caption("Atirador de Elite")

        #Determina a cor de fundo da tela
        self.color = ((255, 255, 255))

        #Inicia a instacia Rocket
        self.rocket = Rocket(self)

        #Cria um Grupo(lista) para a instacia Misseis
        self.misseis = pygame.sprite.Group()

    
    def _check_events(self):
        """Checa os eventos do teclado e do mouse"""
        #Iniciando o modulo get para capturar evento
        for event in pygame.event.get():

            #Evento de sair do jogo, caso seja fechada a tela no close
            if event.type == pygame.QUIT:
                #sai do jogo
                sys.exit()
            
            #Evento quando o botao do mouse e clicado
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #chama a função auxiliar que atira um missel
                self._fire_missil()
            
            #Evento disponivel, não utilizado
            elif event.type == pygame.MOUSEBUTTONUP:
                pass

            #Evento quando qualquer botão do teclado é apertado
            elif event.type == pygame.KEYDOWN:
                #chama a função que verica qual tecla do teclado foi acionada
                self._check_keydown_events(event)

            #Evento quando qualquer botão do teclado é solto
            elif event.type == pygame.KEYUP:
                #chama a função que verica qual tecla do teclado foi desacionada
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        """Checa qual tecla do teclado foi acionada"""

        #Checando se foi a tecla up
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        
        #Checando se foi a tecla down
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    
    def _check_keyup_events(self, event):
        """Checa qual tecla do teclado foi desacionada"""

        #Checando se foi a tecla up
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False

        #Checando se foi a tecla down
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    
    def _update_screen(self):
        """Faz uma atualização ciclica da tela
        Para atualização do componentes da tela"""

        #Limpa a tela
        self.tela.fill(self.color)

        #Desenha o grupo de misseis na posição atual
        for missil in self.misseis.sprites():
            missil.draw_missel()
        
        #Desenha foguete na posição atual
        self.rocket.blitme()

        #Atualiza a tela
        pygame.display.flip()

    
    def _fire_missil(self):
        """Desenha um novo missel na tela
        Se a quantidade de misseis não for ultrapassada"""

        #Condição para desenhar novo missel
        if len(self.misseis) < 5:
            #Cria uma instacia Missel 
            new_missil = Missil(self)

            #Adiciona o novo missel ao grupo misseis
            self.misseis.add(new_missil)

    
    def _update_misseis(self):
        """Atualiza a posição dos misseis na tela"""

        #Chama a função de atualização da instancia Missel
        self.misseis.update()

        #Apaga os misseis que ja sairam do range da tela
        for missel in self.misseis.copy():
            if missel.rect.right >= self.tela.get_rect().right:
                self.misseis.remove(missel)


    def run_game(self):
        """Cria um laço inifito para rodar o Jogo
        Chama as funções do jogo"""

        #loop infinito
        while True:

            #Funçao de checar eventos teclado e mouse
            self._check_events()

            #Função de atualização do Foguete
            self.rocket.update()

            #Função de atualização dos misseis
            self._update_misseis()

            #Função de atualização da tela
            self._update_screen()

            #Taxa de flames da tela
            self.clock.tick(120)


#########################################################
#                                                       #
#                Jogo Atirador de Elite                 #
#                                                       #
#########################################################

if __name__ == "__main__":
    game_shooter = Shooter()
    game_shooter.run_game()