import pygame
import imagens_jogo
from configuracoes import ESPESSURA,CAIXA_FALA,TELA_PC,ALTURA,ATTACKS, PERSONAGEM_TAM 




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
    def __init__(self, img,sprites,projeteis,anima_ataque):
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

        if self.rect.bottom < 0:
            self.kill()

class upgrade(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, bottom, assets, nome):
        # Construtor da classe m??e (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a anima????o do upgrade
        self.up_prof = assets[nome]

        # Inicia o processo de anima????o colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o ??ndice atual na anima????o
        self.image = self.up_prof[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        #coordenadas 
        self.rect.centerx = center
        self.rect.bottom = bottom  

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # pr??xima imagem da anima????o ser?? mostrada
        self.frame_ticks = 150

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudan??a de frame.
        elapsed_ticks = now - self.last_update

        # Se j?? est?? na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avan??a um quadro.
            self.frame += 1

            # Verifica se j?? chegou no final da anima????o.
            if self.frame == len(self.up_prof):
                # Se sim, some da tela
                self.kill()
            else:
                # Se ainda n??o chegou ao fim da anima????o, troca de imagem.
                center = self.rect.center
                self.image = self.up_prof[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center