# -*- coding: utf-8 -*-
'Vamos definir um tamanho para a tela do jogo'
WIDTH = 1000
HEIGHT = 720
TELA_ATUAL = 0
FUNDO_ATUAL = 0
ESTADO_ANTERIOR = 0

'Vamos definir uma velocidade, um tempo de recarga entre ataques e uma altura máxima de pulo para o personagem'
VEL_PERSONAGEM = 15
VEL_KUNAI = 30
RECARGA = 50
PULO_PERSONAGEM = 100
POS_X = 0
POS_Y = 0
WIDTH_P = 105
HEIGHT_P = 130
VIDA_PERSONAGEM = 3
'Posiçoes: 0-Parado Direita / 1-Parado Esquerda / 2-Andando Direita / 3-Andando Esquerda / 4-Pulo Direita / 5-Pulo Esquerda / 6-Ataque Direita / 7-Ataque Esquerda'
'8-Abaixado Direita / 9-Abaixado Esquerda / 10-Kunai Direita / 11 - Kunai Esquerda'
STATUS_PERSONAGEM = 0

'Vamos definir uma velocidade para os inimigos'
VEL_INIMIGO_H = -100
HUMANO_POS_X = 0
HUMANO_POS_Y = 0
VIDA_P = 2
VIDA_CHEFE = 5
RECARGA_INIMIGO = 20
VEL_SCROLL = 300

'Vamos definir uma gravidade que irá atuar sobre o personagem'
GRAVIDADE = 100

'Vamos definir a altura do solo'
HEIGHT_S = 0

PONTUACAO = 0

GAME_STATE = 0