# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Pulo'
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 2
# Define a velocidade inicial no pulo
JUMP_SIZE = 30
# Define a altura do chão
GROUND = HEIGHT * 5 // 6

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
Flying = False
GAMEOVER= False

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, x_coordinate, y_coordinate):  
        pygame.sprite.Sprite.__init__(self)  
          
        # code to initialize variables for sprite bird animation  
        # ...  
        # ...  
        # ...  
  
        # defining the initial velocity of the bird  
        self.velocity = 0  
        self.pressed = False  
      
    # defining a function to handle the animation  
    def update(self):  
        # if the bird is flying then run this code  
        if Flying == True:  
            # adding gravity to the bird  
            # incrementing the velocity of the bird  
            self.velocity += 0.5  
  
            # if the velocity of the bird is greater than 8.5  
            # then set the final value to 8.5  
            if self.velocity > 8.5:  
                self.velocity = 8.5  
            # if the rectangle's bottom is less than 576  
            # then increment its y-axis value by velocity's integer value   
            if self.rect.bottom < 576:  
                self.rect.y += int(self.velocity)  
  
        # if the game is not over then run this code  
        if GAMEOVER == False:  
            # if the mouse button is clicked  
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:  
                # setting the pressed variable value to True  
                self.pressed = True  
                # setting the velocity to -10  
                self.velocity = -10  
  
            # if the mouse button is released  
            if pygame.mouse.get_pressed()[0] == 0:  
                # setting the pressed variable value to False  
                self.pressed = False  
  
            # ...  
            # ...  
            # ...  
            # the sprite animation's update() function code  
              
            # rotating the bird  
            self.image = pygame.transform.rotate(self.image_list[self.index], self.velocity * -2)  
        # if the game is over  
        else:  
            # rotating the bird to -90  
            self.image = pygame.transform.rotate(self.image_list[self.index], -90)  
    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega imagem
    player_img = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()

    # Cria Sprite do jogador
    player = Player(player_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump()

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize a tecla "ESPAÇO" ou seta para cima para pular.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
