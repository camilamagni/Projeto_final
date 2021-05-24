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
atacar1 = pygame.image.load("imagens/Atacar.png")
atacar1 = pygame.transform.scale(atacar1, (ESPESSURA,170))

#----- textos para aparecer no jogo ----
font = pygame.font.SysFont(None, 48)
life = 100
Hp = font.render('paciência:{0}'.format(life), True, (255,255,255))

game = True # condicao para o jogo continuar rodando

clock = pygame.time.Clock()
FPS = 30 #define velocidade dos quadros do jogo 
ATAQUE = 0
DEFESA = 1
FUGIR = 2
ATACAR = 3
ESTADO = ATAQUE
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
            if event.key == pygame.K_RIGHT:
                ESTADO = ATACAR
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
        elif event.type == pygame.KEYUP and ESTADO == ATACAR:
            if event.key == pygame.K_LEFT:
                ESTADO = ATAQUE

    # atualiza a caixa de diálogo

    if ESTADO == ATAQUE:
            window.fill((0, 0, 0))  
            window.blit(background, (0, 0))
            window.blit(Hp, (0, 396))
            window.blit(ataque,(0,430))
    elif ESTADO == DEFESA:
            window.fill((0, 0, 0))
            window.blit(background, (0, 0))
            window.blit(defesa,(0,430))
    elif ESTADO == FUGIR:
            window.fill((0, 0, 0))  
            window.blit(background, (0, 0))
            window.blit(fugir,(0,430))
    elif ESTADO == ATACAR:
            window.fill((0, 0, 0))  
            window.blit(background, (0, 0))
            window.blit(atacar1,(0,430))


    pygame.display.update()