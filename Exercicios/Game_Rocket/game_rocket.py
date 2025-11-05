import sys
import pygame


class Game_Rocket:
    """Jogo que movimenta um foguete na tela"""

    ##################################################Funções do Jogo##########################################################

    def __init__(self):
        """Inicializando atributos do jogo"""
        ##################################Variaveis do Jogo########################################
        pygame.init()
        self.clock = pygame.time.Clock()

        #tamanho da tela
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 245, 230)

        #imagem da tela
        self.image = pygame.image.load('rocket.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.screen.get_rect().midbottom

        #titulo da tela
        pygame.display.set_caption("Rocket Launcher")

        #######################################Variaveis da Imagem ########################################################

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def run_game(self):
        """Inicializa o Jogo"""

        while True:

            self._check_events()
            self.update()  
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""

         # Watch for keyboard and mouse events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Respond to keypresses down."""

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.moving_right = True

        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.moving_left = True
        
        elif event.key == pygame.K_UP:
            # Move the ship to the left.
            self.moving_up = True
        
        elif event.key == pygame.K_DOWN:
            # Move the ship to the left.
            self.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()        
    
    def _check_keyup_events(self, event):
        """Respond to keypresses up."""

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.moving_right = False

        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.moving_left = False
        
        elif event.key == pygame.K_UP:
            # Move the ship to the left.
            self.moving_up = False
        
        elif event.key == pygame.K_DOWN:
            # Move the ship to the left.
            self.moving_down = False


    ###############################################Funções da Imagem do Foguete############################################
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and (self.image_rect.right < self.screen.get_rect().right):
            self.image_rect.x += 4
        if self.moving_left and self.image_rect.left > 0:
            self.image_rect.x -= 4
        if self.moving_up and (self.image_rect.top > self.screen.get_rect().top):
            self.image_rect.y -= 4
        if self.moving_down and (self.image_rect.bottom < self.screen.get_rect().bottom):
            self.image_rect.y += 4
        
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)


gr = Game_Rocket()
gr.run_game()


