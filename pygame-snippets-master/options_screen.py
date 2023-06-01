import pygame
import random
from os import path

ASSETS = {}
back_img = 'background_img'
WIDTH = 1024
HEIGHT = 768
ASSETS[back_img] = pygame.image.load('img/options.jpg')


def options_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    background = ASSETS[back_img]
    background = pygame.transform.scale(background,(WIDTH, HEIGHT))

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(60)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = 2
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    state = 1
                    running = False
            


            

        # A cada loop, redesenha o fundo
        screen.fill((0,0,0))

        screen.blit(background,(0,0))
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
