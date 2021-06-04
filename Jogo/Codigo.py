import pygame
import random

pygame.init()

# ------Gerar a tela do jogo --------
ALTURA = 600
ESPESSURA = 720

imagens = {}
window = pygame.display.set_mode((ESPESSURA, ALTURA))

fala_inicial = pygame.image.load('imagens/ct_introducao.jpg')
imagens['fala_inicial'] = pygame.transform.scale(fala_inicial,(720,150))
fala_inicial2 = pygame.image.load('imagens/ct_introducao2.jpg')
imagens['fala_inicial2'] = pygame.transform.scale(fala_inicial2,(720,150))
decisao = pygame.image.load('imagens/ct_assistir_anime.jpg')
imagens['anime'] = pygame.transform.scale(decisao,(720,150))
decisao2 = pygame.image.load('imagens/ct_estudar_dessoft.jpg')
imagens['estudar'] = pygame.transform.scale(decisao2,(720,150))
decisao3 = pygame.image.load('imagens/ct_dormir_mais.jpg')
imagens['dormir'] = pygame.transform.scale(decisao3,(720,150))
pos_anime1 = pygame.image.load('imagens/ct_pos_anime_anime.png')
imagens['pos_anime_anime'] = pygame.transform.scale(pos_anime1,(720,150))
pos_anime2 = pygame.image.load('imagens/ct_pos_anime_estudar_dessoft.png')
imagens['pos_anime_estudar'] = pygame.transform.scale(pos_anime2,(720,150))
sad_anime =  pygame.image.load('imagens/ct_pos_anime_sad.png')
imagens['sad_anime'] = pygame.transform.scale(sad_anime,(720,150))
sad_anime2 =  pygame.image.load('imagens/ct_pos_anime_sad2.png')
imagens['sad_anime2'] = pygame.transform.scale(sad_anime2,(720,150))
anime_e_estudar = pygame.image.load('imagens/ct_pos_anime_estudar_estudar.jpg')
imagens['estudar_pos_anime'] = pygame.transform.scale(anime_e_estudar,(720,150))
estudar = pygame.image.load('imagens/ct_pos_estudar.jpg')
imagens['pos_estudar'] = pygame.transform.scale(estudar,(720,150))
ganha_proef = pygame.image.load('imagens/ct_proef.jpg')
imagens['proficiente'] = pygame.transform.scale(ganha_proef,(720,150))

continua_estud_sim = pygame.image.load('imagens/ct_continuar_sim.jpg')
imagens['continua_sim'] = pygame.transform.scale(continua_estud_sim,(720,150))
continua_estud_nao = pygame.image.load('imagens/ct_continuar_nao.jpg')
imagens['continua_nao'] = pygame.transform.scale(continua_estud_nao,(720,150))
recomeco = pygame.image.load('imagens/ct_recomeco.jpg')
imagens['recomeco'] = pygame.transform.scale(recomeco,(720,150))


background = pygame.image.load('imagens/fundo_galaxia.jpg').convert()

imagens['background'] = pygame.transform.scale(background, (ESPESSURA, ALTURA))
ataque = pygame.image.load("imagens/ct_ATAQUE.png")
imagens['ataque'] = pygame.transform.scale(ataque, (ESPESSURA,170))
defesa = pygame.image.load("imagens/ct_DEFESA.png")
imagens['defesa'] = pygame.transform.scale(defesa, (ESPESSURA,170))
fugir = pygame.image.load("imagens/ct_DESISTIR.png")
imagens['fugir'] = pygame.transform.scale(fugir, (ESPESSURA,170))
#atacar1 = pygame.image.load("imagens/Atacar.png")
#imagens['atacar1'] = pygame.transform.scale(atacar1, (ESPESSURA,170))
toshi = pygame.image.load("imagens/Toshi_clear.png")
imagens['toshi'] = pygame.transform.scale(toshi, (150,150))
dano = pygame.image.load("imagens/dano.png")
imagens['dano'] =  pygame.transform.scale(dano, (ESPESSURA,170))
personagem = pygame.image.load('imagens/Paola.png').convert_alpha()
imagens['personagem'] = pygame.transform.scale(personagem, (100,100))
quarto = pygame.image.load('imagens/quarto.jpg')
imagens['quarto'] = pygame.transform.scale(quarto, (ESPESSURA, ALTURA))
anima_ataque = pygame.image.load('imagens/binario2.png').convert()
anima_ataque =pygame.transform.scale(anima_ataque, (50,50))
personagem_quarto = pygame.image.load('imagens/Paola2_back.png').convert_alpha()
imagens['personagem_quarto'] = pygame.transform.scale(personagem_quarto,(100,100))

#----- textos para aparecer no jogo ----
font = pygame.font.SysFont(None, 48)
life = 100
paciencia = font.render('paciência:{0}'.format(life), True, (255,255,255))
life2 = 0
Dp = font.render('Dp:{0}'.format(life2), True, (255,255,255)) 

font2 = pygame.font.SysFont(None, 32)
prof= 10
proficiencia = font2.render('proficiência:{0}'.format(prof), True, (255,255,255))

up_prof = []

for i in range(8):
    # Os arquivos de animação são numerados de 00 a 08
    foto = 'imagens/up/mais_15_{}.png'.format(i+1)
    upgrade = pygame.image.load(foto).convert()
    upgrade = pygame.transform.scale(upgrade, (32, 32))
    up_prof.append(upgrade)
imagens['up_prof'] = up_prof

class Toshi(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 150
        self.rect.bottom = 210

class Toshi2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = ESPESSURA/2
        self.rect.bottom = ALTURA - 400


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

class upgrade(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, bottom, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação do upgrade
        self.up_prof = assets['up_prof']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.up_prof[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        #coordenadas 
        self.rect.centerx = center
        self.rect.bottom = bottom  

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # próxima imagem da animação será mostrada
        self.frame_ticks = 150

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.up_prof):
                # Se sim, some da tela
                self.kill()
            else:
                # Se ainda não chegou ao fim da animação, troca de imagem.
                center = self.rect.center
                self.image = self.up_prof[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

sprites = pygame.sprite.Group()
projeteis = pygame.sprite.Group()
toshis = pygame.sprite.Group()
toshis_bravos = pygame.sprite.Group()
acao = pygame.sprite.Group()

up_prof_sprite = pygame.sprite.Group()

avatar =  personagem(imagens['personagem'],sprites,projeteis,anima_ataque)

avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,anima_ataque)

vilao = Toshi(imagens['toshi'])

vilao2 = Toshi2(imagens['toshi'])
up_prof = upgrade(150,500,imagens)
up_prof_sprite.add(up_prof)

sprites.add(avatar)
acao.add(avatar2)
toshis.add(vilao)
toshis_bravos.add(vilao2)

game = True # condicao para o jogo continuar rodando

clock = pygame.time.Clock()
FPS = 30 #define velocidade dos quadros do jogo 

ATAQUE = 0
DEFESA = 1
FUGIR = 2
ATACAR = 3
CONTRAATAQUE = 4
ACAO_ATAQUE = 5
QUARTO = 6
QUARTO2 = 7
ANIME = 8
ESTUDAR = 9
DORMIR = 10
ANIME_ANIME = 11
ANIME_ESTUD = 12
SAD_ANIME = 13
SAD_ANIME2 = 14
ANIME_ESTUDAR_ESTUDAR = 15
ESTUDAR_ESTUDAR = 16
GANHA_PONTO = 17
CONTINUAR_SIM = 18
CONTINUAR_NAO = 19 
RECOMECAR = 20
ESTADO = QUARTO


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
        elif event.type == pygame.KEYUP and ESTADO == QUARTO:
            if event.key == pygame.K_RETURN:
                ESTADO = QUARTO2
        elif event.type == pygame.KEYUP and ESTADO == QUARTO2:
            if event.key == pygame.K_RETURN:
                ESTADO = ANIME
        elif event.type == pygame.KEYUP and ESTADO == ANIME:
            if event.key == pygame.K_DOWN:
                ESTADO = ESTUDAR
            if event.key == pygame.K_UP:
                ESTADO = DORMIR
            if event.key == pygame.K_RETURN:
                ESTADO = ANIME_ANIME
        elif event.type == pygame.KEYUP and ESTADO == ESTUDAR:
            if event.key == pygame.K_DOWN:
                ESTADO = DORMIR
            if event.key == pygame.K_UP:
                ESTADO = ANIME
            if event.key == pygame.K_RETURN:
                ESTADO = ESTUDAR_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == DORMIR:
            if event.key == pygame.K_DOWN:
                ESTADO = ANIME
            if event.key == pygame.K_UP:
                ESTADO = ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == ANIME_ANIME :
            if event.key == pygame.K_DOWN:
                ESTADO = ANIME_ESTUD
            if event.key == pygame.K_UP:
                ESTADO = ANIME_ESTUD
            if event.key == pygame.K_RETURN:
                ESTADO = SAD_ANIME
        elif event.type == pygame.KEYUP and ESTADO == SAD_ANIME:
            if event.key == pygame.K_RETURN:
                ESTADO = SAD_ANIME2
        elif event.type == pygame.KEYUP and ESTADO == ANIME_ESTUD:
            if event.key == pygame.K_DOWN:
                ESTADO = ANIME_ANIME
            if event.key == pygame.K_UP:
                ESTADO = ANIME_ANIME
            if event.key == pygame.K_RETURN:
                ESTADO = ANIME_ESTUDAR_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_ESTUDAR:
            if event.key == pygame.K_RETURN:
                ESTADO = GANHA_PONTO
                prof += 15
                proficiencia = font2.render('proficiência:{0}'.format(prof), True, (255,255,255))
        elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO:
            if event.key == pygame.K_RETURN:
                ESTADO = CONTINUAR_SIM
        elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_SIM:
            if event.key == pygame.K_UP:
                ESTADO = CONTINUAR_NAO
            if event.key == pygame.K_DOWN:
                ESTADO = CONTINUAR_NAO
        elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_NAO:
            if event.key == pygame.K_UP:
                ESTADO = CONTINUAR_SIM
            if event.key == pygame.K_DOWN:
                ESTADO = CONTINUAR_SIM
        elif event.type == pygame.KEYUP and ESTADO == SAD_ANIME2:
            if event.key == pygame.K_RETURN:
                ESTADO == RECOMECAR       

    hits = pygame.sprite.spritecollide(vilao2,projeteis, True)
    if len(hits) > 0:
        ESTADO = CONTRAATAQUE   

    if ESTADO == QUARTO:
        window.fill((0, 0, 0))
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['fala_inicial'], (0, 0))   
    elif ESTADO == QUARTO2:
        window.fill((0, 0, 0))
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['fala_inicial2'], (0, 0))
    elif ESTADO == ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ANIME_ESTUDAR_ESTUDAR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['estudar_pos_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ANIME_ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['pos_anime_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ANIME_ESTUD:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['pos_anime_estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == RECOMECAR:
        window.fill((0, 0, 0))
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['recomeco'], (0, 0))
    elif ESTADO == CONTINUAR_SIM:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['continua_sim'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == CONTINUAR_NAO:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['continua_nao'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == SAD_ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['sad_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ESTUDAR_ESTUDAR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['pos_estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == GANHA_PONTO:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['proficiente'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == SAD_ANIME2:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['sad_anime2'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ESTUDAR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == DORMIR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['dormir'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ATAQUE:    
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            toshis.draw(window)
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['ataque'],(0,430))
    elif ESTADO == DEFESA:
            window.fill((0, 0, 0))
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            toshis.draw(window)
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['defesa'],(0,430))
    elif ESTADO == FUGIR:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            toshis.draw(window)
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['fugir'],(0,430))
    elif ESTADO == ATACAR:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            toshis.draw(window)
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['atacar1'],(0,430))
    elif ESTADO == CONTRAATAQUE:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            sprites.draw(window)
            toshis_bravos.draw(window)
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))
            window.blit(imagens['dano'],(0,430))
    elif ESTADO == ACAO_ATAQUE:
            window.fill((0, 0, 0))  
            window.blit(imagens['background'], (0, 0))
            acao.draw(window)
            projeteis.draw(window)
            toshis_bravos.draw(window)
            window.blit(paciencia, (0, 396))
            window.blit(Dp, (ESPESSURA-110, 0))

    if ESTADO == GANHA_PONTO:
        up_prof_sprite.draw(window)
        up_prof_sprite.update()

    sprites.update()
    acao.update()
    toshis_bravos.update()
    toshis.update()
    pygame.display.update()