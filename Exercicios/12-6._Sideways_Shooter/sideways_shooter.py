import sys
from time import sleep
import pygame
from rocket import Rocket
from missil import Missil
from nave_inimiga import Enemy


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

        self.font_size = 100
        self.font = pygame.font.Font(None, self.font_size)
        self.posicao_mensagem = (400,300)
        self.cor_mensagem = (0, 0, 0)
        self.mensagem = "GAME OVER"
        self.imprimir = self.font.render(self.mensagem, True, self.cor_mensagem)

        self.game_over = False
        
        #Inicia a instacia Rocket
        self.rocket = Rocket(self)

        #Cria um Grupo(lista) para a instacia Misseis
        self.misseis = pygame.sprite.Group()
        self.atirar = False
        self.intervalo = False
        self.tempo_intervalo = 0

        #Cria um grupo de naves inimigas para combate
        self.naves_inimigas1 = pygame.sprite.Group()
        self.naves_inimigas2 = pygame.sprite.Group()
        self.velocidade = 1
        self.direction1 = 0
        self.direction2 = 0

        self.tentativas = 0
        self.chances = 2

        self._create_fleet()

    
    def _check_events(self):
        """Checa os eventos do teclado e do mouse"""
        #Iniciando o modulo get para capturar evento
        for event in pygame.event.get():

            if self.game_over:
                sleep(2)

            #Evento de sair do jogo, caso seja fechada a tela no close
            if event.type == pygame.QUIT or self.game_over:
                #sai do jogo
                sys.exit()
            
            #Evento quando o botao do mouse e clicado
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #chama a função auxiliar que atira um missel
                self.atirar = True
            
            #Evento disponivel, não utilizado
            elif event.type == pygame.MOUSEBUTTONUP:
                self.atirar = False
                self.intervalo = False
                self.tempo_intervalo = 0
            
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

        #Desenha nave inimiga
        self.naves_inimigas1.draw(self.tela)
        self.naves_inimigas2.draw(self.tela)

        if self.tentativas >= self.chances:
            #Imprime a mensagem de GAME OVER
            self.tela.blit(self.imprimir, self.posicao_mensagem)
            self.game_over = True

        #Atualiza a tela
        pygame.display.flip()

    
    def _fire_missil(self):
        """Desenha um novo missel na tela
        Se a quantidade de misseis não for ultrapassada"""

        #Condição para desenhar novo missel
        if len(self.misseis) < 10000:
            #Cria uma instacia Missel 
            new_missil = Missil(self)

            #Adiciona o novo missel ao grupo misseis
            self.misseis.add(new_missil)

    
    def _update_misseis(self):
        """Atualiza a posição dos misseis na tela"""
        
        if self.atirar:
            if not self.intervalo:
                self._fire_missil()
                self.intervalo = True
            self.tempo_intervalo += 1
            if self.tempo_intervalo == 15:
                self.intervalo = False
                self.tempo_intervalo = 0

        #Chama a função de atualização da instancia Missel
        self.misseis.update()

        #Apaga os misseis que ja sairam do range da tela
        for missel in self.misseis.copy():
            if missel.rect.right >= self.tela.get_rect().right:
                self.misseis.remove(missel)
        
        #Verifica se houve colisões
        self._check_colisao_missil()
    
    
    def _create_fleet(self):
        if self.tentativas < self.chances:
            nave_inimiga = Enemy(self)
            current_x = (self.tela.get_rect().width - nave_inimiga.rect.width)
            current_y = 0
            i = 0
            while current_x > 300:
                while current_y < 800: 
                    self._create_nave_inimiga(current_x, current_y, i)
                    current_y += 2 * nave_inimiga.rect.height
                i += 1
                if (i % 2) == 0:
                    current_y = 0
                else:
                    current_y = nave_inimiga.rect.height

                current_x -= nave_inimiga.rect.width
        

    def _create_nave_inimiga(self,position_x, position_y, grupo):
        new_nave = Enemy(self)
        new_nave.rect.x = position_x
        new_nave.rect.y = position_y
        if grupo % 2 == 0:
            self.naves_inimigas1.add(new_nave)
        else:
            self.naves_inimigas2.add(new_nave)    
    

    def _update_nave_inimiga(self):
            
        self.direction1 = self._check_fim_de_tela(self.naves_inimigas1, self.direction1)
        for nave in self.naves_inimigas1.sprites():
            nave.y = float(nave.rect.y)
            nave.y += 1 * self.direction1
            nave.rect.y = nave.y
        self.naves_inimigas1.update()
        self._check_colisao_naves_inimigas(self.naves_inimigas1)
        self.direction2 = self._check_fim_de_tela(self.naves_inimigas2, self.direction2)
        for nave in self.naves_inimigas2.sprites():
            nave.y = float(nave.rect.y)
            nave.y += 1 * self.direction2
            nave.rect.y = nave.y
        self.naves_inimigas2.update()
        self._check_colisao_naves_inimigas(self.naves_inimigas2)

  
    def _check_colisao_naves_inimigas(self, naves_inimigas):

        left_colide = False

        for nave in naves_inimigas.sprites():
            if nave.rect.left <= 0:
                left_colide = True
                break

        if (pygame.sprite.spritecollideany(self.rocket, naves_inimigas)) or left_colide:
            
            self.tentativas += 1
            
            self.misseis.empty()
            self.naves_inimigas1.empty()
            self.naves_inimigas2.empty()

            self._create_fleet()
            self.rocket.reposition()

            sleep(1)


    def _check_fim_de_tela(self, checar_nave, direcao):

        for nave in checar_nave.sprites():
            if nave.deteccao_fim_tela() == 1:
                return 1
            
            elif nave.deteccao_fim_tela() == -1:
                return -1
        
        return direcao


    def _check_colisao_missil(self):

        colisao1 = pygame.sprite.groupcollide(self.misseis, self.naves_inimigas1, True, True)
        
        colisao2 = pygame.sprite.groupcollide(self.misseis, self.naves_inimigas2, True, True)

        if (not self.naves_inimigas1) and (not self.naves_inimigas2) :
            self.misseis.empty()
            self.velocidade += 1 
            self._create_fleet()
          

    def run_game(self):
        """Cria um laço inifito para rodar o Jogo
        Chama as funções do jogo"""

        #loop infinito
        while True:

            #Funçao de checar eventos teclado e mouse
            self._check_events()

            if self.tentativas < self.chances:
                #Função de atualização do Foguete
                self.rocket.update()

                #Função de atualização dos misseis
                self._update_misseis()

                #Função de atualização das naves inimigas
                self._update_nave_inimiga()
            

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