# -- coding: utf-8 --

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
mp3_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Fundo em Movimento'
WIDTH = 1024 # Largura da tela
HEIGHT = 768 # Altura da tela
FPS = 60 # Frames por segundo
PLAYER_IMG = 'player_img'
BLOCK_IMG = 'block_img'
BACKGROUND_IMG = 'background_img'

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a velocidade inicial do mundo
world_speed = -5

# Outras constantes
INITIAL_BLOCKS = 1
TILE_SIZE = 80

# Define a aceleração da gravidade
GRAVITY = 1
# Define a velocidade inicial no pulo
JUMP_SIZE = 20
# Define a altura do chão
GROUND = 768

# Define estados possíveis do jogador
STILL = 0

randyblock = random.randrange(-834, -503, 52)


# Class que representa as rodas/canos
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, x, y, speedx):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        #tile_img = pygame.transform.scale(tile_img, (100, 300))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = 1024
        self.rect.y = randyblock

        self.speedx = speedx

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0:
            randyblock = random.randrange(-834, -503, 52)
            self.rect.x += (1024 + 162) * 1.5
            self.rect.y = randyblock


class Tile2(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, x, y, speedx, block):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        #tile_img = pygame.transform.scale(tile_img, (100, 300))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = randyblock + 1150

        self.speedx = speedx

        self.block = block

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0:
            self.rect.x += (1024 + 162) * 1.5
            self.rect.y = self.block.rect.y + 1150

class Tile3(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, x, y, speedx):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        #tile_img = pygame.transform.scale(tile_img, (100, 300))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = randyblock

        self.speedx = speedx

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0:
            randyblock = random.randrange(-834, -503, 52)
            self.rect.x += 1024
            self.rect.y = randyblock

class Tile4(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, x, y, speedx, block):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        #tile_img = pygame.transform.scale(tile_img, (100, 300))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = randyblock + 1150

        self.speedx = speedx

        self.block = block

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0:
            self.rect.x += 1024
            self.rect.y = self.block.rect.y + 1150


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.state = STILL
        # Aumenta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (150, 100))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Começa no centro da janela
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = int(HEIGHT * 7 / 8)

        # Começa no topo da janela e cai até o chão
        self.rect.centerx = WIDTH / 2
        self.rect.top = 0

        self.speedy = 0
        
    def update(self):
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        #if self.speedy > 0:
            #self.state = FALLING
            #self.speedy -= JUMP_SIZE
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = STILL

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = STILL


# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'Meu_projeto.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, 'rodas.png')).convert_alpha()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, 'background-1.png')).convert()
    pygame.mixer.music.load(path.join(img_dir, 'lotus72.mp3'))
    pygame.mixer.music.set_volume(0.4)
    return assets


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG])
    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo para guardar somente os sprites do mundo (obstáculos, objetos, etc).
    # Esses sprites vão andar junto com o mundo (fundo)
    world_sprites = pygame.sprite.Group()
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BLOCKS):
        block_x = 1024
        block_y = randyblock
        block2_x = 1024
        block2_y = randyblock + 1150
        block3_x = (1024 + 162) * 1.5
        block3_y = randyblock
        block4_x = (1024 + 162) * 1.5
        block4_y = randyblock + 1150
        block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
        block2 = Tile2(assets[BLOCK_IMG], block2_x, block2_y, world_speed, block)
        block3 = Tile3(assets[BLOCK_IMG], block3_x, block3_y, world_speed)
        block4 = Tile4(assets[BLOCK_IMG], block4_x, block4_y, world_speed, block3)
        world_sprites.add(block, block2, block3, block4)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(block, block2, block3, block4)

    PLAYING = 0
    DONE = 1

    state = PLAYING
    pygame.mixer.music.play(loops=-1)
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump() 

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # Verifica se algum bloco saiu da janela
        # for block in world_sprites:
        #     if block.rect.right < 0:
        #         # Destrói o bloco e cria um novo no final da tela
        #         block.rect.x = 1024
        #         block.rect.y = randyblock
        #         print(block.rect.y)

        # for block2 in world_sprites:
        #     if block2.rect.right < 0:
        #         block2.rect.x = 1024
        #         block2.rect.y = 0
        #         print(block2.rect.y)
        
        

        # for block3 in world_sprites:
        #     if block3.rect.right < 0:
        #         block3.rect.x = 1024
        #         block3.rect.y = randyblock

        # for block4 in world_sprites:
        #     if block4.rect.right < 0:
        #         block4.rect.x = 1024
        #         block4.rect.y = 0

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Atualiza a posição da imagem de fundo.
        background_rect.x += world_speed
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

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
print('Este exemplo não é interativo.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()