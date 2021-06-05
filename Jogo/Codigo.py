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

final_dia = pygame.image.load('imagens/fim_dia1.jpg')
imagens['FIM_DIA_SO_ANIME'] = pygame.transform.scale(final_dia,(720,150))
na_cadeira = pygame.image.load('imagens/Paola_cadeira_clear.png').convert_alpha()
imagens['na_cadeira'] = pygame.transform.scale(na_cadeira, (100,100))
shingeki = pygame.image.load('imagens/shingeki.jpg')
imagens['shingeki'] = pygame.transform.scale(shingeki, (50,55))
academia_python = pygame.image.load('imagens/academia_python.jpg')
imagens['academia'] = pygame.transform.scale(academia_python, (50,55))
pontos_20 = pygame.image.load('imagens/ct_20_pontos.png')
imagens['proficiente20'] = pygame.transform.scale(pontos_20,(720,150))

pontos_10 = pygame.image.load('imagens/ct_10_pontos.png')
imagens['proficiente10'] = pygame.transform.scale(pontos_10,(720,150))
fim_dia_anime_estudar = pygame.image.load('imagens/ct_fim_dia_anime_estudar.jpg')
imagens['fim_dia_anime_estudar'] = pygame.transform.scale(fim_dia_anime_estudar,(720,150))
fim_dia_so_estudar = pygame.image.load('imagens/ct_fim_dia_so_estudo.jpg')
imagens['fim_dia_so_estudar'] = pygame.transform.scale(fim_dia_anime_estudar,(720,150))
anime_nao_estudar_serie = pygame.image.load('imagens/ct_anime_nao_estudar_serie.jpg')
imagens['anime_nao_estudar_serie'] = pygame.transform.scale(anime_nao_estudar_serie,(720,150))
anime_nao_estudar_dormir = pygame.image.load('imagens/ct_anime_nao_estudar_dormir.jpg')
imagens['anime_nao_estudar_dormir'] = pygame.transform.scale(anime_nao_estudar_dormir,(720,150))
series = pygame.image.load('imagens/series_plat.jpg')
imagens['series'] = pygame.transform.scale(series, (50,55))
acorda_tarde = pygame.image.load('imagens/ct_acordou_tarde_serie.jpg')
imagens['acordou_tarde_serie'] =  pygame.transform.scale(acorda_tarde, (720,150))
dormir_mais = pygame.image.load('imagens/ct_dormir_muito.jpg')
imagens['dormir_muito'] = pygame.transform.scale(dormir_mais, (720,150))
dia2_estudar = pygame.image.load('imagens/dia2_estudar.jpg')
imagens['dia2_estudar'] = pygame.transform.scale(dia2_estudar, (720,150))
dia2_dormir = pygame.image.load('imagens/dia2_dormir.jpg')
imagens['dia2_dormir'] = pygame.transform.scale(dia2_dormir, (720,150))
dia2_anime = pygame.image.load('imagens/dia2_anime.jpg')
imagens['dia2_anime'] = pygame.transform.scale(dia2_anime, (720,150))
estudar_serie = pygame.image.load('imagens/ct_estudar_serie.jpg')
imagens['estudar_serie'] = pygame.transform.scale(estudar_serie, (720,150))
estudar_dormir = pygame.image.load('imagens/ct_estudar_dormir.jpg')
imagens['estudar_dormir'] = pygame.transform.scale(estudar_dormir, (720,150))
serie_dormir = pygame.image.load('imagens/ct_serie_dormir.jpg')
imagens['serie_dormir'] = pygame.transform.scale(serie_dormir, (720,150))
estudou_muito = pygame.image.load('imagens/ct_estudou_muito.jpg')
imagens['estudou_muito'] = pygame.transform.scale(estudou_muito, (720,150))





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
up_prof15 = []
up_prof10 = []
up_prof20 = []

for i in range(8):
    # Os arquivos de animação são numerados de 1 a 8
    imagem15 = 'imagens/up/mais_15_{}.png'.format(i+1)
    imagem10 = 'imagens/up/mais_10_{}.png'.format(i+1)
    imagem20 = 'imagens/up/mais_20_{}.png'.format(i+1)
    upgrade15 = pygame.image.load(imagem15).convert()
    upgrade10 = pygame.image.load(imagem10).convert()
    upgrade20 = pygame.image.load(imagem20).convert()
    upgrade10 = pygame.transform.scale(upgrade10, (32, 32))
    upgrade15 = pygame.transform.scale(upgrade15, (32, 32))
    upgrade20 = pygame.transform.scale(upgrade20, (32, 32))
    up_prof15.append(upgrade15)
    up_prof10.append(upgrade10)
    up_prof20.append(upgrade20)

imagens['up_prof15'] = up_prof15
imagens['up_prof10'] = up_prof10
imagens['up_prof20'] = up_prof20
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
    def __init__(self, center, bottom, assets, nome):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação do upgrade
        self.up_prof = assets[nome]

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

up_prof_sprite15 = pygame.sprite.Group()
up_prof_sprite10 = pygame.sprite.Group()
up_prof_sprite20 = pygame.sprite.Group()

avatar =  personagem(imagens['personagem'],sprites,projeteis,anima_ataque)

avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,anima_ataque)

vilao = Toshi(imagens['toshi'])

vilao2 = Toshi2(imagens['toshi'])

up_prof15_class = upgrade(150,500,imagens, 'up_prof15')
up_prof_sprite15.add(up_prof15_class)

up_prof10_class = upgrade(150,500,imagens, 'up_prof10')
up_prof_sprite10.add(up_prof10_class)

up_prof20_class = upgrade(150,500,imagens, 'up_prof20')
up_prof_sprite20.add(up_prof20_class)


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
GANHA_PONTO15 = 17
CONTINUAR_SIM = 18
CONTINUAR_NAO = 19 
RECOMECAR = 20
FIM_DIA_SO_ANIME = 21
GANHA_PONTO20 = 22
GANHA_PONTO10 = 23
CONTINUAR_SIM_1 = 24
CONTINUAR_NAO_1 = 25
GANHA_PONTO15_1 = 26
FIM_DIA_ANIME_E_ESTUDA = 27
ANIME_NAO_SERIE = 28
ANIME_NAO_DORMIR = 29
ANIME_SERIE = 30 
DORMIR_MUITO = 31
DIA2_ANIME = 32
DIA2_ESTUDAR = 33
DIA2_DORMIR = 34
ESTUDAR_DORMIR = 35
ESTUDAR_SERIE = 36
SERIE_DORMIR = 37
ESTUDOU_MUITO = 38
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
                life2 -= 20
                Dp = font.render('Dp:{}'.format(life2), True, (255,255,255))    
                ESTADO = ACAO_ATAQUE
        elif event.type == pygame.KEYUP and ESTADO == CONTRAATAQUE:
            if event.key == pygame.K_RETURN:
                ESTADO = ATAQUE
                life -= 15
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
            if event.key == pygame.K_RETURN:
                ESTADO = DORMIR_MUITO
        elif event.type == pygame.KEYUP and ESTADO == DORMIR_MUITO:
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == DIA2_ESTUDAR:
            if event.key == pygame.K_DOWN:
                ESTADO = DIA2_ANIME
            if event.key == pygame.K_UP:
                ESTADO = DIA2_DORMIR
            if event.key == pygame.K_RETURN:
                ESTADO = ESTUDAR_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == DIA2_ANIME:
            if event.key == pygame.K_DOWN:
                ESTADO = DIA2_DORMIR
            if event.key == pygame.K_UP:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == DIA2_DORMIR:
            if event.key == pygame.K_DOWN:
                ESTADO = DIA2_ESTUDAR
            if event.key == pygame.K_UP:
                ESTADO = DIA2_ANIME
                
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
        elif event.type == pygame.KEYUP and ESTADO == SAD_ANIME2:
            if event.key == pygame.K_RETURN:
                ESTADO = FIM_DIA_SO_ANIME
        elif event.type == pygame.KEYUP and ESTADO == FIM_DIA_SO_ANIME:
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == ANIME_ESTUD:
            if event.key == pygame.K_DOWN:
                ESTADO = ANIME_ANIME
            if event.key == pygame.K_UP:
                ESTADO = ANIME_ANIME
            if event.key == pygame.K_RETURN:
                ESTADO = ANIME_ESTUDAR_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_ESTUDAR:
            if event.key == pygame.K_RETURN:
                ESTADO = GANHA_PONTO10
                prof += 10
                proficiencia = font2.render('proficiência:{0}'.format(prof), True, (255,255,255))
        elif event.type == pygame.KEYUP and ESTADO == ANIME_ESTUDAR_ESTUDAR:
            if event.key == pygame.K_RETURN:
                ESTADO = GANHA_PONTO15
                prof += 15
                proficiencia = font2.render('proficiência:{0}'.format(prof), True, (255,255,255))
        elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO15:
            if event.key == pygame.K_RETURN:
                ESTADO = CONTINUAR_SIM
        elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO10:
            if event.key == pygame.K_RETURN:
                ESTADO = CONTINUAR_SIM_1
        elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_SIM:
            if event.key == pygame.K_UP:
                ESTADO = CONTINUAR_NAO
            if event.key == pygame.K_DOWN:
                ESTADO = CONTINUAR_NAO
            if event.key == pygame.K_RETURN:
                ESTADO = GANHA_PONTO20
                prof += 20
                proficiencia = font2.render('proficiência:{0}'.format(prof), True, (255,255,255))

        elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO20:
            if event.key == pygame.K_RETURN:
                ESTADO = ESTUDOU_MUITO
        elif  event.type == pygame.KEYUP and ESTADO == ESTUDOU_MUITO:
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_SIM_1:
            if event.key == pygame.K_UP:
                ESTADO = CONTINUAR_NAO_1
            if event.key == pygame.K_DOWN:
                ESTADO = CONTINUAR_NAO_1
            if event.key == pygame.K_RETURN:
                ESTADO = GANHA_PONTO15_1
                prof += 15
                proficiencia = font2.render('proficiência:{0}'.format(prof), True, (255,255,255)) 
        elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_NAO_1:
            if event.key == pygame.K_UP:
                ESTADO = CONTINUAR_SIM_1
            if event.key == pygame.K_DOWN:
                ESTADO = CONTINUAR_SIM_1
            if event.key == pygame.K_RETURN:
                ESTADO = ANIME_NAO_SERIE
        elif event.type == pygame.KEYUP and ESTADO == ANIME_NAO_SERIE:
            if event.key == pygame.K_RETURN:
                ESTADO = ANIME_SERIE
            if event.key == pygame.K_UP:
                ESTADO = ANIME_NAO_DORMIR
            if event.key == pygame.K_DOWN:
                ESTADO = ANIME_NAO_DORMIR
        elif event.type == pygame.KEYUP and ESTADO == ANIME_SERIE:
            if event.key == pygame.K_RETURN:
                ESTADO = SERIE_DORMIR
        elif event.type == pygame.KEYUP and ESTADO == ANIME_NAO_DORMIR:
            if event.key == pygame.K_UP:
                ESTADO = ANIME_NAO_SERIE
            if event.key == pygame.K_DOWN:
                ESTADO = ANIME_NAO_SERIE
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO15_1:
            if event.key == pygame.K_RETURN:
                ESTADO = FIM_DIA_ANIME_E_ESTUDA
        elif event.type == pygame.KEYUP and ESTADO == FIM_DIA_ANIME_E_ESTUDA:
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_NAO:
            if event.key == pygame.K_UP:
                ESTADO = CONTINUAR_SIM
            if event.key == pygame.K_DOWN:
                ESTADO = CONTINUAR_SIM
        elif event.type == pygame.KEYUP and ESTADO == SAD_ANIME2:
            if event.key == pygame.K_RETURN:
                ESTADO = ESTUDAR_SERIE
        elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_SERIE:
            if event.key == pygame.K_UP:
                ESTADO = ESTUDAR_DORMIR
            if event.key == pygame.K_DOWN:
                ESTADO = ESTUDAR_DORMIR
            if event.key == pygame.K_RETURN:
                ESTADO = SERIE_DORMIR
        elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_DORMIR:
            if event.key == pygame.K_UP:
                ESTADO = ESTUDAR_SERIE
            if event.key == pygame.K_DOWN:
                ESTADO = ESTUDAR_SERIE
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        elif event.type == pygame.KEYUP and ESTADO == SERIE_DORMIR:
            if event.key == pygame.K_RETURN:
                ESTADO = DIA2_ESTUDAR
        if  event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                ESTADO = ANIME

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
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['estudar_pos_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
        window.blit(imagens['academia'],(145,370))
    elif ESTADO == ANIME_ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['pos_anime_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
        window.blit(imagens['shingeki'],(145,370))

    elif ESTADO == ANIME_SERIE:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['acordou_tarde_serie'], (0, 0))
        window.blit(imagens['series'],(145,370))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == ANIME_ESTUD:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['pos_anime_estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
        window.blit(imagens['shingeki'],(145,370))
    elif ESTADO == RECOMECAR:
        window.fill((0, 0, 0))
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['recomeco'], (0, 0))
    elif ESTADO == CONTINUAR_SIM:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['continua_sim'], (0, 0))
        window.blit(imagens['academia'],(145,370))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == CONTINUAR_NAO:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['continua_nao'], (0, 0))
        window.blit(imagens['academia'],(145,370))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == CONTINUAR_SIM_1:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['continua_sim'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == CONTINUAR_NAO_1:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['continua_nao'], (0, 0))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == ESTUDAR_DORMIR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['estudar_dormir'], (0, 0))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == ESTUDAR_SERIE:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['estudar_serie'], (0, 0))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == SERIE_DORMIR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (270, 400))
        window.blit(imagens['serie_dormir'], (0, 0))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == SAD_ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['sad_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ESTUDAR_ESTUDAR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['pos_estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
        window.blit(imagens['academia'],(145,370))
    elif ESTADO == GANHA_PONTO15:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['proficiente'], (0, 0))
        window.blit(proficiencia, (10, 500))
        up_prof_sprite15.draw(window)
        up_prof_sprite15.update()

    elif ESTADO == GANHA_PONTO15_1:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['proficiente'], (0, 0))
        window.blit(proficiencia, (10, 500))
        up_prof_sprite15.draw(window)
        up_prof_sprite15.update()

    elif ESTADO == GANHA_PONTO20:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['proficiente20'], (0, 0))
        window.blit(imagens['academia'],(145,370))
        window.blit(proficiencia, (10, 500))
        up_prof_sprite20.draw(window)
        up_prof_sprite20.update()

    elif ESTADO == GANHA_PONTO10:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['proficiente10'], (0, 0))
        window.blit(proficiencia, (10, 500))
        up_prof_sprite10.draw(window)
        up_prof_sprite10.update()


    elif ESTADO == ANIME_NAO_SERIE:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['anime_nao_estudar_serie'], (0, 0))
        window.blit(imagens['academia'],(145,370))
        window.blit(proficiencia, (10, 500))   
    elif ESTADO == ANIME_NAO_DORMIR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['na_cadeira'], (270, 400))
        window.blit(imagens['anime_nao_estudar_dormir'], (0, 0))
        window.blit(imagens['academia'],(145,370))
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
    elif ESTADO == DORMIR_MUITO:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['dormir_muito'], (0, 0))
        window.blit(proficiencia, (10, 500))

    elif ESTADO == FIM_DIA_SO_ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['FIM_DIA_SO_ANIME'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == FIM_DIA_ANIME_E_ESTUDA:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['fim_dia_anime_estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == DIA2_ANIME:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['dia2_anime'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == DIA2_DORMIR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['dia2_dormir'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == DIA2_ESTUDAR:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['dia2_estudar'], (0, 0))
        window.blit(proficiencia, (10, 500))
    elif ESTADO == ESTUDOU_MUITO:
        window.blit(imagens['quarto'], (0, 0))
        window.blit(imagens['personagem_quarto'], (500, 390))
        window.blit(imagens['estudou_muito'], (0, 0))
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

    sprites.update()
    acao.update()
    toshis_bravos.update()
    toshis.update()
    pygame.display.update()