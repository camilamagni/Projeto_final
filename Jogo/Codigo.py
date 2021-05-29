import pygame

pygame.init()

# ------Gerar a tela do jogo --------
ALTURA = 600
ESPESSURA = 720

window = pygame.display.set_mode((ESPESSURA, ALTURA))

imagens = {}
background = pygame.image.load('imagens/fundo.jpg').convert()
imagens['background'] = pygame.transform.scale(background, (ESPESSURA, ALTURA))
ataque = pygame.image.load("imagens/ataque.jpeg")
imagens['ataque'] = pygame.transform.scale(ataque, (ESPESSURA,170))
defesa = pygame.image.load("imagens/defesa.jpeg")
imagens['defesa'] = pygame.transform.scale(defesa, (ESPESSURA,170))
fugir = pygame.image.load("imagens/fugir.jpeg")
imagens['fugir'] = pygame.transform.scale(fugir, (ESPESSURA,170))
atacar1 = pygame.image.load("imagens/Atacar.png")
imagens['atacar1'] = pygame.transform.scale(atacar1, (ESPESSURA,170))
toshi = pygame.image.load("imagens/toshi.png")
imagens['toshi'] = pygame.transform.scale(toshi, (150,150))
imagens['dano'] =  pygame.image.load("imagens/dano.png")
personagem = pygame.image.load('imagens/Paola.png').convert_alpha()
imagens['personagem'] = pygame.transform.scale(personagem, (100,100))
anima_ataque = pygame.image.load('imagens/binario2.png').convert()
anima_ataque =pygame.transform.scale(anima_ataque, (110,110))

#----- textos para aparecer no jogo ----
font = pygame.font.SysFont(None, 48)
life = 100
paciencia = font.render('paciência:{0}'.format(life), True, (255,255,255))
life2 = 100
Dp = font.render('Dp:{0}'.format(life2), True, (255,255,255)) 

class personagem(pygame.sprite.Sprite):
    def __init__(self, img, sprites, projeteis, anima_ataque):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = ESPESSURA - 70
        self.rect.bottom = ALTURA - 130
        self.sprites = sprites
        self.projeteis = projeteis
        self.anima_ataque = anima_ataque

    def ataque(self):
        codigos = projetil(self.anima_ataque, self.rect.top, self.rect.centerx)
        self.sprites.add(codigos)
        self.projeteis.add(codigos)

class personagem2(pygame.sprite.Sprite):
    def __init__(self, img,sprites,projeteis,anima_ataque):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = ESPESSURA/2
        self.rect.bottom = ALTURA - 130
        self.sprites = sprites
        self.projeteis = projeteis
        self.anima_ataque = anima_ataque

    def ataque(self):
        codigos = projetil(self.anima_ataque, self.rect.top, self.rect.centerx)
        self.sprites.add(codigos)
        self.projeteis.add(codigos)

class projetil(pygame.sprite.Sprite):
    def __init__(self,img,bottom,centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom <0:
            self.kill()


sprites = pygame.sprite.Group()
projeteis = pygame.sprite.Group()

acao = pygame.sprite.Group()
avatar =  personagem(imagens['personagem'],sprites,projeteis,anima_ataque)
avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,anima_ataque)
sprites.add(avatar)
acao.add(avatar2)

game = True # condicao para o jogo continuar rodando

clock = pygame.time.Clock()
FPS = 30 #define velocidade dos quadros do jogo 

ATAQUE = 0
DEFESA = 1
FUGIR = 2
ATACAR = 3
CONTRAATAQUE = 4
ACAO_ATAQUE = 5

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
            if event.key == pygame.K_RETURN:
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
            if event.key == pygame.K_RETURN:
                avatar2.ataque()
                life2-=20
                Dp = font.render('Dp:{}'.format(life2), True, (255,255,255))    
                ESTADO = ACAO_ATAQUE
        elif event.type == pygame.KEYUP and ESTADO == CONTRAATAQUE:
            if event.key == pygame.K_RETURN:
                ESTADO = ATAQUE
                life-=15
                paciencia = font.render('paciencia:{0}'.format(life), True,(255,255,255))

    # atualiza a caixa de diálogo

    if ESTADO == ATAQUE:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            window.blit(imagens['toshi'], (0, 210))
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['ataque'],(0,430))
    elif ESTADO == DEFESA:
            window.fill((0, 0, 0))
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            window.blit(imagens['toshi'], (0, 210))
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['defesa'],(0,430))
    elif ESTADO == FUGIR:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            window.blit(imagens['toshi'], (0, 210))
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['fugir'],(0,430))
    elif ESTADO == ATACAR:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            window.blit(imagens['toshi'], (0, 210))
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['atacar1'],(0,430))
    elif ESTADO == CONTRAATAQUE:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            window.blit(imagens['toshi'], (0, 210))
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['dano'],(0,430))
    elif ESTADO == ACAO_ATAQUE:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            acao.draw(window)
            projeteis.draw(window)
            window.blit(imagens['toshi'], (0, 210))
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))

    sprites.update()
    acao.update()
    pygame.display.update()