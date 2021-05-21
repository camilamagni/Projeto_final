import pygame
pygame.init()
# ------Gerar a tela do jogo --------
ALTURA = 600
ESPESSURA = 480
window = pygame.display.set_mode((ESPESSURA, ALTURA))
background = pygame.image.load('imagens/fundo.jpg').convert()
background = pygame.transform.scale(background, (ESPESSURA, ALTURA))
ataque = pygame.image.load("imagens/ataque.jpeg")
ataque = pygame.transform.scale(ataque, (ESPESSURA,170))
defesa = pygame.image.load("imagens/defesa.jpeg")
defesa = pygame.transform.scale(defesa, (ESPESSURA,170))
fugir = pygame.image.load("imagens/fugir.jpeg")
fugir = pygame.transform.scale(fugir, (ESPESSURA,170))
game = True # condicao para o jogo continuar rodando

clock = pygame.time.Clock()
FPS = 30 #define velocidade dos quadros do jogo 
ATAQUE = 0
DEFESA = 1
FUGIR = 2
while game:
    clock.tick(FPS)
    # ---- verifica os eventos que acontecem no jogo
    for event in pygame.event.get():
        # ----- define o que acontece com os eventos que ocorrem
        if event.type == pygame.QUIT:
            game = False
        # ações para alterar a caixa de diálogo
        if event.type == pygame.KEYUP and ESTADO == ATAQUE:
            if event.key == pygame.K_UP:
                ESTADO = FUGIR
            if event.key == pygame.K_DOWN:
                ESTADO = DEFESA 
        elif event.type == pygame.KEYUP and ESTADO == DEFESA:
            if event.key == pygame.K_UP:
                ESTADO = ATAQUE
            if event.key == pygame.K_DOWN:
                ESTADO = FUGIR
        elif event.type == pygame.KEYUP and ESTADO == FUGIR:
            if event.key == pygame.K_UP:
                ESTADO = DEFESA
            if event.key == pygame.K_DOWN:
                ESTADO = ATAQUE

    window.fill((255, 255, 255)) 
    window.blit(background, (0, 0))
    pygame.display.update()