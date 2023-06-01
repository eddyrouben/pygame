import pygame
import random
from os import path

ASSETS = {}
back_img = 'background_img'
score_font ='score_font'
WIDTH = 1024
HEIGHT = 768
ASSETS[back_img] = pygame.image.load('img/final.jpg')
YELLOW = (255, 255, 0)


def final_screen(screen, score):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    background = ASSETS[back_img]
    background = pygame.transform.scale(background,(WIDTH, HEIGHT))


    font = pygame.font.Font('img/PressStart2P.ttf', 28)

    


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
                if event.key == pygame.K_s:
                    state = 1
                    running = False
            


            

        # A cada loop, redesenha o fundo
        screen.fill((0,0,0))
        
        screen.blit(background,(0,0))

        # Cria o texto do score
        text = font.render(str(score), True, (255, 255, 0))
        text_rect = text.get_rect(center=(512, (768//2) - 50))

        # A cada loop, redesenha o fundo
        screen.blit(text, text_rect)


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
