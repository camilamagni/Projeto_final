import pygame
pygame.init()
# ------Gerar a tela do jogo --------
ALTURA = 600
ESPESSURA = 480
window = pygame.display.set_mode((ESPESSURA, ALTURA))

game = True # condicao para o jogo continuar rodando

clock = pygame.time.Clock()
FPS = 30 #define velocidade dos quadros do jogo 

while game:
    clock.tick(FPS)
    # ---- verifica os eventos que acontecem no jogo
    for event in pygame.event.get():
        # ----- define o que acontece com os eventos que ocorrem
        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255)) #vai preencher a tela de branco
    pygame.display.update()