# from typing import NewType, Pattern
from estrutura_jogo import tela_jogo
from configuracoes import ALTURA,ESPESSURA
import pygame
import random


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((ESPESSURA, ALTURA))
pygame.display.set_caption('PyToshi Fight')

tela_jogo(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados