from configuracoes import ESPESSURA,CAIXA_FALA,TELA_PC,ALTURA,ATTACKS, PERSONAGEM_TAM ,FPS
from classes import Toshi,Toshi2, personagem, personagem2 , projetil,upgrade
from imagens_jogo import load_perifericos,anima_ataque
import pygame
import random





def tela_jogo(window):

    imagens = load_perifericos()
        
    game = True # condicao para o jogo continuar rodando

    clock = pygame.time.Clock()
   # Musicas e sons do jogo
    pygame.mixer.music.load('sons/Musica_tema.mp3')
    pygame.mixer.music.set_volume(0.15)
    rise_and_shine = pygame.mixer.Sound('sons/Rise_and_shinee.mp3')
    Boss_battle = pygame.mixer.Sound('sons/Boos_battle.mp3')
    Boss_battle.set_volume(0.25)
    sasageyo = pygame.mixer.Sound('sons/Sasageyooo_official.mp3')
    naruto_sad = pygame.mixer.Sound('sons/Naruto_sad_funk_jogo.mp3')
    netflix = pygame.mixer.Sound('sons/Netflix.mp3')
    upgrade_som = pygame.mixer.Sound('sons/upgrade_real.mp3')
    star_wars = pygame.mixer.Sound('sons/tema_inicial.mp3')
    winamo = pygame.mixer.Sound('sons/win.mp3')
    sad_fim =  pygame.mixer.Sound('sons/Sad_bugado.mp3')
   #------- SPRITES ----------
    sprites = pygame.sprite.Group()
    projeteis = pygame.sprite.Group()
    toshis = pygame.sprite.Group()
    toshis_bravos = pygame.sprite.Group()
    acao = pygame.sprite.Group()
    up_prof_sprite15 = pygame.sprite.Group()
    up_prof_sprite10 = pygame.sprite.Group()
    up_prof_sprite20 = pygame.sprite.Group()


    avatar =  personagem(imagens['personagem'],sprites,projeteis,anima_ataque)


    vilao = Toshi(imagens['toshi'])

    vilao2 = Toshi2(imagens['toshi'])

    up_prof15_class = upgrade(150,500,imagens, 'up_prof15')
    up_prof_sprite15.add(up_prof15_class)

    up_prof10_class = upgrade(150,500,imagens, 'up_prof10')
    up_prof_sprite10.add(up_prof10_class)

    up_prof20_class = upgrade(150,500,imagens, 'up_prof20')
    up_prof_sprite20.add(up_prof20_class)

    sprites.add(avatar)
    toshis.add(vilao)
    toshis_bravos.add(vilao2)

    #----- textos para aparecer no jogo ----
    font = pygame.font.SysFont(None, 48)
    estresse = 0
    paciencia = font.render('Estresse:{0}'.format(estresse), True, (255,255,255))

    life2 = 0
    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255)) 

    font2 = pygame.font.SysFont(None, 32)
    prof= 10
    proficiencia = font2.render('Proficiência:{0}'.format(prof), True, (255,255,255))
    # ESTADOS DO JOGO

    INICIO = 0
    FICOU_DP = 1
    PASSOU = 2

    QUARTO = 6 #Começo do jogo, com a data do dia 12/06 
    QUARTO2 = 7 # Segunda fala do jogo
    ANIME = 8 #Abre o primeiro menu de escolhas dentro do jogo selecionado na ação anime
    ESTUDAR = 9 #Abre o primeiro menu de escolhas dentro do jogo selecionado na ação estudar
    DORMIR = 10 #Abre o primeiro menu de escolhas dentro do jogo selecionado na ação dormir
    ANIME_ANIME = 11 #Coloca o personagem na cadeira com um anime na tela do computador com a mensagem de que o episodio acabou selecionando o continuar vendo anime
    ANIME_ESTUD = 12 #Coloca o personagem na cadeira com um anime na tela do computador com a mensagem de que o episodio acabou selecionando o estudar
    SAD_ANIME = 13 #Escolhendo continuar anime e mostrar o quanto vc perdeu tempo
    SAD_ANIME2 = 14 # mostra o quanto vc se sente vazio ao terminar o seu anime :( 
    ANIME_ESTUDAR_ESTUDAR = 15 #O personagem fica na cadeira mas troca de anime para academia python
    ESTUDAR_ESTUDAR = 16  #Coloca o personagem na cadeira , para academia python, sendo primeira escolha do dia antece ganha15
    GANHA_PONTO15 = 17  #Ganha 15 de proficiencia
    CONTINUAR_SIM = 18 #Pergunta se o jogador quer continuar selecionado SIIIM
    CONTINUAR_NAO = 19 #Pergunta se o jogador quer continuar selecionado nao, antecede estudar_serie
    RECOMECAR = 20
    FIM_DIA_SO_ANIME = 21 #fim do dia só quando vc só assiste anime ;-; 
    GANHA_PONTO20 = 22 #Ganha 20 de proficiencia depois de continuar_sim
    GANHA_PONTO10 = 23 #Ganha 10 de proficiencia
    CONTINUAR_SIM_1 = 24 #Depois de ganha 10 de proficiencia, pergunta se vc quer continuar estudando
    CONTINUAR_NAO_1 = 25 #Depois de ganha 10 de proficiencia, pergunta se vc quer nao continuar estudando
    GANHA_PONTO15_1 = 26 # Se você continua estudando ganha 15 ponto de proficiencia
    FIM_DIA_ANIME_E_ESTUDA = 27 #se vc assite 1 ep e estuda o res
    ANIME_NAO_SERIE = 28 #Você escolhe parar de estudar e selecionado serie
    ANIME_NAO_DORMIR = 29 #Você escolhe parar de estudar e selecionado dormir
    ANIME_SERIE = 30 # se vc seleciona serie  vem para ca
    DORMIR_MUITO = 31 #escolher dormir de primeira coisa no dia 
    DIA2_ANIME = 32 #RISE AND SHINEEEEE PRIMEIRA FALA DO SEGUNDO DIAA , SELECIONANDO ANIME
    DIA2_ESTUDAR = 33 #RISE AND SHINEEEEE PRIMEIRA FALA DO SEGUNDO DIAA, SELECIONANDO ESTUDAR
    DIA2_DORMIR = 34 #RISE AND SHINEEEEE PRIMEIRA FALA DO SEGUNDO DIAA, SELECIONANDO DORMIR 
    ESTUDAR_DORMIR = 35 # pergunta se quer dormir
    ESTUDAR_SERIE = 36 #pergunta se quer ver serie
    SERIE_DORMIR = 37 #final do dia quando escolhe serie apos estudar uma vez 
    ESTUDOU_MUITO = 38 #Depois de ganha 20 potno
    DIA3 = 39 #inicia o dia que você está ocupado o dia inteiro 
    PRE_TOSHI = 40
    ATAQUE1_DIC =41
    ATAQUE1_FOR =42
    ATAQUE1_INPUT =43
    ATAQUE1_WHILE =44
    ATAQUE2_DIC =45
    ATAQUE2_IFELSE =46
    ATAQUE2_LISTA =47
    ATAQUE2_INPUT =48
    ATAQUE3_FOR =49
    ATAQUE3_IFELSE =50
    ATAQUE3_LISTA =51
    ATAQUE3_WHILE =52
    DIMINUIR_ESTRESSE = 62
    ESTRESSADAH = 63
    NAO_PODE = 64 

    ATAQUE = 53
    DEFESA = 54
    DESISTIR = 55
    CONTRAATAQUE = 56
    ACAO_ATAQUE = 57

    LOOP = 58
    INVALIDO = 59
    RANGE_ERRADO =  60
    SEM_CONDICAO = 61   

    ESTADO = INICIO

    contador_loko = 1
    sad = 1
    entrada = 1
    dias = 1
    ordem_ataque = 1
    conta_sasa = 1
    musica_inicial = 1
    fim_bom = 1
    fim_dp =1 
    conta_defesa = 0
    
    situacao = {}

    situacao['atacar_while'] = imagens['loop']
    situacao['atacar_for'] = imagens['range_errado']
    situacao['atacar_input'] = imagens['invalido']
    situacao['atacar_dicionario'] = imagens['invalido']    
    situacao['atacar_ifelse'] = imagens['sem_condicao']
    situacao['atacar_lista'] = imagens['indice_errado']


    while game:
        clock.tick(FPS)
        # ---- verifica os eventos que acontecem no jogo
        for event in pygame.event.get():
            # ----- define o que acontece com os eventos que ocorrem
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYUP and ESTADO == INICIO:
                if event.key == pygame.K_RETURN:
                    ESTADO = QUARTO
                    star_wars.stop()
                    pygame.mixer.music.play(loops=-1)


            elif event.type == pygame.KEYUP and ESTADO == ATAQUE:
                if event.key == pygame.K_UP:
                    ESTADO = DESISTIR
                if event.key == pygame.K_DOWN:
                    ESTADO = DEFESA
                if event.key == pygame.K_RETURN and ordem_ataque == 1:
                    ESTADO = ATAQUE1_WHILE
                    ordem_ataque+=1
                elif event.key == pygame.K_RETURN and ordem_ataque == 2:
                    ESTADO = ATAQUE2_INPUT
                    ordem_ataque+=1
                elif event.key == pygame.K_RETURN and ordem_ataque == 3:
                    ESTADO = ATAQUE3_LISTA
                    ordem_ataque = 1
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE1_WHILE:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE1_DIC
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE1_FOR
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_while'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255)) 
                    attack = 'atacar_while'
                    ESTADO = ACAO_ATAQUE

            elif event.type == pygame.KEYUP and ESTADO == ATAQUE1_FOR:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE1_WHILE
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE1_INPUT
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_for'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_for'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE1_INPUT:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE1_FOR
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE1_DIC
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_input'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255)) 
                    attack = 'atacar_input'
                    ESTADO = ACAO_ATAQUE

            elif event.type == pygame.KEYUP and ESTADO == ATAQUE1_DIC:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE1_INPUT
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE1_WHILE
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_dicionario'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_dicionario'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE2_INPUT:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE2_IFELSE
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE2_LISTA
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_input'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_input'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE2_LISTA:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE2_INPUT
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE2_DIC
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_lista'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_lista'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE2_DIC:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE2_LISTA
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE2_IFELSE
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_dicionario'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255)) 
                    attack = 'atacar_dicionario'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE2_IFELSE:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE2_DIC
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE2_INPUT
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_ifelse'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_ifelse'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE3_LISTA:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE3_WHILE
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE3_IFELSE
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_lista'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_lista'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE3_IFELSE:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE3_LISTA
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE3_FOR
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_ifelse'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255)) 
                    attack = 'atacar_ifelse'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE3_FOR:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE3_IFELSE
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE3_WHILE
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_for'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_for'
                    ESTADO = ACAO_ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == ATAQUE3_WHILE:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE3_FOR
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE3_LISTA
                if event.key == pygame.K_RETURN:
                    avatar2 =  personagem2(imagens['personagem'],sprites,projeteis,imagens['atacar_while'])
                    acao.add(avatar2)
                    avatar2.ataque()
                    life2 += ((5 + prof/10)* (100-estresse)/100)
                    if life2 >= 100:
                        life2 = 100
                    Dp = font.render('Nota:{0}'.format(life2), True, (255,255,255))
                    attack = 'atacar_while'
                    ESTADO = ACAO_ATAQUE



            elif event.type == pygame.KEYUP and ESTADO == DEFESA:
                if event.key == pygame.K_UP:
                    ESTADO = ATAQUE
                if event.key == pygame.K_DOWN:
                    ESTADO = DESISTIR
                if event.key == pygame.K_RETURN and conta_defesa <2:
                    ESTADO = DIMINUIR_ESTRESSE
                    if estresse < 15:
                        estresse = 0
                    else:
                        estresse -= 15
                    paciencia = font.render('Estresse:{0}'.format(estresse), True,(255,255,255))
                    conta_defesa+=1
                elif event.key == pygame.K_RETURN and conta_defesa >= 2:
                    ESTADO = NAO_PODE
            elif event.type == pygame.KEYUP and ESTADO == DESISTIR:
                if event.key == pygame.K_UP:
                    ESTADO = DEFESA
                if event.key == pygame.K_DOWN:
                    ESTADO = ATAQUE
                if event.key == pygame.K_RETURN:
                    ESTADO = FICOU_DP
            elif event.type == pygame.KEYUP and ESTADO == CONTRAATAQUE:
                if event.key == pygame.K_RETURN:
                    ESTADO = ATAQUE
                    if prof > 85:
                        estresse += 8
                        paciencia = font.render('Estresse:{0}'.format(estresse), True,(255,255,255))
                    else:
                        estresse += 20
                        paciencia = font.render('Estresse:{0}'.format(estresse), True,(255,255,255))

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
                if event.key == pygame.K_RETURN and dias ==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if   event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1
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
                if event.key == pygame.K_RETURN:
                    ESTADO = ANIME_ANIME
            elif event.type == pygame.KEYUP and ESTADO == DIA2_DORMIR:
                if event.key == pygame.K_DOWN:
                    ESTADO = DIA2_ESTUDAR
                if event.key == pygame.K_UP:
                    ESTADO = DIA2_ANIME
                if event.key == pygame.K_RETURN:
                    ESTADO = DORMIR_MUITO
            
            elif event.type == pygame.KEYUP and ESTADO == ANIME_ANIME :
                if event.key == pygame.K_DOWN:
                    ESTADO = ANIME_ESTUD
                if event.key == pygame.K_UP:
                    ESTADO = ANIME_ESTUD
                if event.key == pygame.K_RETURN:
                    ESTADO = SAD_ANIME
                    conta_sasa = 1
            elif event.type == pygame.KEYUP and ESTADO == SAD_ANIME:
                if event.key == pygame.K_RETURN:
                    ESTADO = SAD_ANIME2
                    sad = 1

            elif event.type == pygame.KEYUP and ESTADO == SAD_ANIME2:
                if event.key == pygame.K_RETURN:
                    ESTADO = FIM_DIA_SO_ANIME
            elif event.type == pygame.KEYUP and ESTADO == FIM_DIA_SO_ANIME:
                naruto_sad.stop()
                if event.key == pygame.K_RETURN and dias ==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if   event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1
            elif event.type == pygame.KEYUP and ESTADO == ANIME_ESTUD:
                if event.key == pygame.K_DOWN:
                    ESTADO = ANIME_ANIME
                if event.key == pygame.K_UP:
                    ESTADO = ANIME_ANIME
                if event.key == pygame.K_RETURN:
                    sasageyo.stop()
                    conta_sasa = 1
                    ESTADO = ANIME_ESTUDAR_ESTUDAR
            elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_ESTUDAR:
                if event.key == pygame.K_RETURN:
                    ESTADO = GANHA_PONTO15
                    prof += 15
                    proficiencia = font2.render('Proficiência:{0}'.format(prof), True, (255,255,255))
                    up_prof15_class.kill()
                    up_prof15_class = upgrade(150,500,imagens, 'up_prof15')
                    up_prof_sprite15.add(up_prof15_class)
                    upgrade_som.play()
            elif event.type == pygame.KEYUP and ESTADO == ANIME_ESTUDAR_ESTUDAR:
                if event.key == pygame.K_RETURN:
                    ESTADO = GANHA_PONTO10
                    prof += 10
                    proficiencia = font2.render('Proficiência:{0}'.format(prof), True, (255,255,255))
                    up_prof10_class.kill()
                    up_prof10_class = upgrade(150,500,imagens, 'up_prof10')
                    up_prof_sprite10.add(up_prof10_class)
                    upgrade_som.play()
            elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO15:
                upgrade_som.stop()
                if event.key == pygame.K_RETURN:
                    ESTADO = CONTINUAR_SIM
            elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO10:
                upgrade_som.stop()
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
                    proficiencia = font2.render('Proficiência:{0}'.format(prof), True, (255,255,255))
                    up_prof20_class.kill()
                    up_prof20_class = upgrade(150,500,imagens, 'up_prof20')
                    up_prof_sprite20.add(up_prof20_class)
                    upgrade_som.play()
            elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO20:
                upgrade_som.stop()
                if event.key == pygame.K_RETURN:
                    ESTADO = ESTUDOU_MUITO
            elif  event.type == pygame.KEYUP and ESTADO == ESTUDOU_MUITO:
                if event.key == pygame.K_RETURN and dias ==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if   event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1 
            elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_SIM_1:
                if event.key == pygame.K_UP:
                    ESTADO = CONTINUAR_NAO_1
                if event.key == pygame.K_DOWN:
                    ESTADO = CONTINUAR_NAO_1
                if event.key == pygame.K_RETURN:
                    ESTADO = GANHA_PONTO15_1
                    prof += 15
                    proficiencia = font2.render('Proficiência:{0}'.format(prof), True, (255,255,255)) 
                    up_prof15_class.kill()
                    up_prof15_class = upgrade(150,500,imagens, 'up_prof15')
                    up_prof_sprite15.add(up_prof15_class)
                    upgrade_som.play()
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
                    netflix.play()
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
                if event.key == pygame.K_RETURN and dias ==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if   event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1
            elif event.type == pygame.KEYUP and ESTADO == GANHA_PONTO15_1:
                upgrade_som.stop()
                if event.key == pygame.K_RETURN:
                    ESTADO = FIM_DIA_ANIME_E_ESTUDA
            elif event.type == pygame.KEYUP and ESTADO == FIM_DIA_ANIME_E_ESTUDA:
                if event.key == pygame.K_RETURN and dias ==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if   event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1
            elif event.type == pygame.KEYUP and ESTADO == CONTINUAR_NAO:
                if event.key == pygame.K_UP:
                    ESTADO = CONTINUAR_SIM
                if event.key == pygame.K_DOWN:
                    ESTADO = CONTINUAR_SIM
                if event.key == pygame.K_RETURN:
                    ESTADO = ESTUDAR_SERIE
            elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_SERIE:
                if event.key == pygame.K_UP:
                    ESTADO = ESTUDAR_DORMIR
                if event.key == pygame.K_DOWN:
                    ESTADO = ESTUDAR_DORMIR
                if event.key == pygame.K_RETURN:
                    ESTADO = SERIE_DORMIR
                    netflix.play()
            elif event.type == pygame.KEYUP and ESTADO == ESTUDAR_DORMIR:
                if event.key == pygame.K_UP:
                    ESTADO = ESTUDAR_SERIE
                if event.key == pygame.K_DOWN:
                    ESTADO = ESTUDAR_SERIE
                if event.key == pygame.K_RETURN and dias ==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if   event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1
            elif event.type == pygame.KEYUP and ESTADO == SERIE_DORMIR:
                if event.key == pygame.K_RETURN and dias==2:
                    ESTADO = DIA3
                    naruto_sad.play()
                if event.key == pygame.K_RETURN and dias ==3:
                    ESTADO = PRE_TOSHI
                elif event.key == pygame.K_RETURN and dias ==1 or dias >2:
                    ESTADO = DIA2_ESTUDAR
                    dias += 1
                    contador_loko = 1
            elif event.type == pygame.KEYUP and ESTADO == DIA3:
                if event.key == pygame.K_RETURN:
                    ESTADO = DIA2_ESTUDAR
                    contador_loko = 1
            elif event.type == pygame.KEYUP and ESTADO == PRE_TOSHI:
                if event.key == pygame.K_RETURN:
                    ESTADO = ATAQUE
                    pygame.mixer.music.stop()
            elif event.type == pygame.KEYUP and ESTADO == DIMINUIR_ESTRESSE:
                if event.key == pygame.K_RETURN:
                    ESTADO = ATAQUE
            elif event.type == pygame.KEYUP and ESTADO == NAO_PODE:
                if event.key == pygame.K_RETURN:
                    ESTADO = ATAQUE
                

            if ESTADO == DIA3 and dias ==2:
                dias+=1

        hits = pygame.sprite.spritecollide(vilao2,projeteis, True)
        if len(hits) > 0:
            numero = random.randint(0,5)
            if numero == 1 or numero == 5 or numero == 3:
                ESTADO = CONTRAATAQUE
            else:
                ESTADO = ATAQUE

        if life2 >= 100:
            ESTADO = PASSOU 
        if estresse >= 100:
            ESTADO = FICOU_DP
                
        if ESTADO == INICIO:
            window.fill((0, 0, 0))
            window.blit(imagens['tela_inicial'], (0, 0))
            if musica_inicial == 1:
                star_wars.play()
                musica_inicial +=1 

        elif ESTADO == QUARTO:
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
            window.blit(imagens['academia'],(145,370))
            window.blit(proficiencia, (10, 500))
        elif ESTADO == ANIME_ANIME:
            window.blit(imagens['quarto'], (0, 0))
            window.blit(imagens['na_cadeira'], (270, 400))
            window.blit(imagens['pos_anime_anime'], (0, 0))
            window.blit(imagens['shingeki'],(145,370))
            window.blit(proficiencia, (10, 500))
            pygame.mixer.music.pause()
            if conta_sasa == 1:
                sasageyo.play()
                conta_sasa+=1
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
            window.blit(imagens['shingeki'],(145,370))
            window.blit(proficiencia, (10, 500))
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
            window.blit(imagens['series'],(145,370))

        elif ESTADO == SAD_ANIME:
            window.blit(imagens['quarto'], (0, 0))
            window.blit(imagens['personagem_quarto'], (500, 390))
            window.blit(imagens['sad_anime'], (0, 0))
            window.blit(proficiencia, (10, 500))
            sasageyo.stop()
            if sad == 1:
                naruto_sad.play()
                sad+=1
        elif ESTADO == ESTUDAR_ESTUDAR:
            window.blit(imagens['quarto'], (0, 0))
            window.blit(imagens['na_cadeira'], (270, 400))
            window.blit(imagens['pos_estudar'], (0, 0))
            window.blit(imagens['academia'],(145,370))
            window.blit(proficiencia, (10, 500))
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
            sasageyo.stop()
            naruto_sad.stop()
            pygame.mixer.music.unpause()
            if contador_loko == 1:
                rise_and_shine.play()
                contador_loko+=1

        elif ESTADO == ESTUDOU_MUITO:
            window.blit(imagens['quarto'], (0, 0))
            window.blit(imagens['personagem_quarto'], (500, 390))
            window.blit(imagens['estudou_muito'], (0, 0))
            window.blit(proficiencia, (10, 500))
        elif ESTADO == DIA3:
            window.blit(imagens['quarto'], (0, 0))
            window.blit(imagens['personagem_quarto'], (500, 390))
            window.blit(imagens['dia3'], (0, 0))
            window.blit(proficiencia, (10, 500))
        elif ESTADO == PRE_TOSHI:
            window.blit(imagens['dia_da_prova'], (0, 0))

        elif ESTADO == ATAQUE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque'],(0,450))
                if entrada ==1:
                    Boss_battle.play(loops=-1)
                    entrada +=1
        elif ESTADO == ATAQUE1_DIC:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque_dicionario'],(0,450))
        elif ESTADO == ATAQUE1_FOR:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque_for'],(0,450))
        elif ESTADO == ATAQUE1_INPUT:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque_input'],(0,450))
        elif ESTADO == ATAQUE1_WHILE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque_while'],(0,450))
        elif ESTADO == ATAQUE2_DIC:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque2_dicionario'],(0,450))
        elif ESTADO == ATAQUE2_IFELSE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque2_ifelse'],(0,450))
        elif ESTADO == ATAQUE2_INPUT:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque2_input'],(0,450))
        elif ESTADO == ATAQUE2_LISTA:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque2_lista'],(0,450))
        elif ESTADO == ATAQUE3_WHILE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque3_while'],(0,450))
        elif ESTADO == ATAQUE3_LISTA:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque3_lista'],(0,450))
        elif ESTADO == ATAQUE3_FOR:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque3_for'],(0,450))
        elif ESTADO == ATAQUE3_IFELSE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['ataque3_ifelse'],(0,450))
        
        elif ESTADO == DEFESA:
                window.fill((0, 0, 0))
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['defesa'],(0,450))
        elif ESTADO == NAO_PODE:
                window.fill((0, 0, 0))
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['nao_pode'],(0,450))
        elif ESTADO == DESISTIR:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['fugir'],(0,450))       
        elif ESTADO == CONTRAATAQUE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis_bravos.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(situacao[attack],(0,400))
        elif ESTADO == ACAO_ATAQUE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                acao.draw(window)
                projeteis.draw(window)
                toshis_bravos.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
        elif ESTADO == LOOP:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis_bravos.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['loop'],(0,400))
        elif ESTADO == INVALIDO:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis_bravos.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['invalido'],(0,400))
        elif ESTADO == RANGE_ERRADO:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis_bravos.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['range_errado'],(0,400))
        elif ESTADO == SEM_CONDICAO:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis_bravos.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['sem_condicao'],(0,400))
        elif ESTADO == DIMINUIR_ESTRESSE:
                window.fill((0, 0, 0))  
                window.blit(imagens['background'], (0, 0))
                sprites.draw(window)
                toshis.draw(window)
                window.blit(paciencia, (10, 400))
                window.blit(Dp, (ESPESSURA-150,0))
                window.blit(imagens['diminui_estresse'],(ESPESSURA/2-125,200))
                window.blit(imagens['defesa'],(0,450))
        elif ESTADO == FICOU_DP:
                Boss_battle.stop()
                window.fill((0, 0, 0))  
                window.blit(imagens['ficou_dp'], (0, 0))
                if fim_dp == 1:
                    sad_fim.play()
                    fim_dp +=1 
        elif ESTADO == PASSOU:
                Boss_battle.stop()
                window.fill((0, 0, 0))  
                window.blit(imagens['passamo'], (0, 0))
                if fim_bom == 1:
                    winamo.play()
                    fim_bom +=1
        elif ESTADO == ESTRESSADAH:
                window.fill((0, 0, 0))
                window.blit(imagens['background'], (0, 0))


                

        sprites.update()
        acao.update()
        toshis_bravos.update()
        toshis.update()
        pygame.display.update()
