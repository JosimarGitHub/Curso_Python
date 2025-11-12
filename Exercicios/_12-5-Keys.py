import sys
import pygame
import time

pygame.init()
resolution = (1200, 800)
capition = "Eventos do Teclado"
tela = pygame.display.set_mode(resolution)
pygame.display.set_caption(capition)
font_size = 36
fonte = pygame.font.Font(None, font_size)
evento = "Aguardando Evento"
sair = False
posicao_texto = (500,200)
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza = (230, 230, 230)
verdadeiro = True

while True:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            evento = f"Tecla pressionada: {pygame.key.name(event.key)}"
        
        elif event.type == pygame.MOUSEMOTION:
            evento = f"Posição do mouse: {pygame.mouse.get_pos()}"

        if evento == "Tecla pressionada: q":
            sair = True
        
    
    if sair:
        tela.fill(branco)
        superficie_texto = fonte.render(evento, True, preto)
        tela.blit(superficie_texto, posicao_texto)
        pygame.display.flip()
        time.sleep(5)
        sys.exit()
    
    tela.fill(cinza)
    superficie_texto = fonte.render(evento, True, preto)
    tela.blit(superficie_texto, posicao_texto)
    pygame.display.flip()

    