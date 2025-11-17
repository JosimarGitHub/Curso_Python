import sys
from time import sleep
import pygame
from rocket import Rocket
from missil import Missil
from target import Target
import button

class TargetShooter:
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

        self.game_over = False
        
        #Inicia a instacia Rocket
        self.rocket = Rocket(self)

        #Cria um Grupo(lista) para a instacia Misseis
        self.misseis = pygame.sprite.Group()

        #Criar um alvo
        self.target = Target(self)

        # Criar um botão
        self.start_button = button.Buttom(self)

        self.encrease_speed = 3
        self.tentativas = 0
        self.chances = 10
        self.points = 1000
        self.run = False


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

                if self.run:
                    #chama a função auxiliar que atira um missel
                    self._fire_missil()

                if not self.run:
                    position_mouse = pygame.mouse.get_pos()
                    if self.start_button.rect.collidepoint(position_mouse):
                        self.points = 0
                        self.encrease_speed = 3
                        self.target.speed = 1
                        self.game_over = False
                        self.run = True
                    
            #Evento disponivel, não utilizado
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            
            elif event.type == pygame.MOUSEMOTION:
                self.rocket.moving = True
                position_mouse = pygame.mouse.get_pos()
                self.rocket.image_y = position_mouse[1]

            #Evento quando qualquer botão do teclado é apertado
            elif event.type == pygame.KEYDOWN:
                #chama a função que verica qual tecla do teclado foi acionada
                #self._check_keydown_events(event)
                pass

            #Evento quando qualquer botão do teclado é solto
            elif event.type == pygame.KEYUP:
                #chama a função que verica qual tecla do teclado foi desacionada
                #self._check_keyup_events(event)
                pass

    
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

        #Desenha um alvo
        self.target.draw_target()

        if not self.run:
        
            if self.game_over:
                '''self.tela.blit(self.imprimir, self.posicao_mensagem)
                self.imprimir2 = self.font2.render(self.pontuacao, True, self.cor_mensagem)
                self.tela.blit(self.imprimir2, self.posicao_mensagem2)'''
                self._imprimir_mensagem(100, 200, "GAME OVER")
                self._imprimir_mensagem(80, 300, self.pontuacao)

            #Desenha um botão de start
            self.start_button.draw()

        if self.tentativas >= self.chances:
            #Imprime a mensagem de GAME OVER
            self.misseis.empty()
            self.tentativas = 0
            self.run = False
            self.game_over = True
            self.pontuacao = "Sua Pontuação foi " + str(self.points) + " pontos"
            print(self.pontuacao)

        #Atualiza a tela
        pygame.display.flip()

    
    def _fire_missil(self):
        """Desenha um novo missel na tela
        Se a quantidade de misseis não for ultrapassada"""

        #Condição para desenhar novo missel
        if len(self.misseis) < 2:
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
                self.tentativas += 1
            target_rect = self.target.rect

            if target_rect.colliderect(missel.rect):
                self.points += 1
                self.misseis.remove(missel)
                if self.points >= self.encrease_speed:
                    self.encrease_speed = self.points + 5
                    self.target.speed += 1

    
    def _imprimir_mensagem(self, font_size, posicao_mensagem, mensagem, cor_mensagem = (0, 0, 0), cor_fundo=None):
        font = pygame.font.Font(None, font_size)
        gerar_imagem = font.render(mensagem, True, cor_mensagem, cor_fundo)
        gerar_imagem_rect = gerar_imagem.get_rect()
        gerar_imagem_rect.centerx = self.tela.get_rect().centerx
        gerar_imagem_rect.y = posicao_mensagem
        self.tela.blit(gerar_imagem, gerar_imagem_rect)

        
    def run_game(self):
        """Cria um laço inifito para rodar o Jogo
        Chama as funções do jogo"""

        #loop infinito
        while True:

            #Funçao de checar eventos teclado e mouse
            self._check_events()

            if self.run and (self.tentativas < self.chances):
                #Função de atualização do Foguete
                self.rocket.update()

                #Função de atualização dos misseis
                self._update_misseis()

                self.target.update()

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
    game_shooter = TargetShooter()
    game_shooter.run_game()