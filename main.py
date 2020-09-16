# -*- coding: utf-8 -*-
from PPlay.window import *
from posicoes import Posicoes
from tela import Tela
import globais
from inimigos import Humano
from PPlay.keyboard import Keyboard
from menu import Menu
from highscore import Pontuacao
from dificuldades import Dificuldade

janela = Window(globais.WIDTH,globais.HEIGHT)

tela = Tela(janela)
tela.setFundo()

teclado = Keyboard()

dificuldade = Dificuldade()
dificuldade.setDificuldade()

humano = Humano(janela)

menu = Menu(janela)

posicoes = Posicoes(janela)

pontuacao = Pontuacao(janela)

while True:
    tela.setTela()

    if(teclado.key_pressed("RIGHT")):
        globais.STATUS_PERSONAGEM = 2
        posicoes.setUpdate()
        while(globais.STATUS_PERSONAGEM == 2):
            if globais.GAME_STATE == 1:
                tela.getFundo()
                posicoes.getUpdate()
                humano.setPosicao()
                humano.setAtaque()
                humano.setInverter()
                humano.colisao()
                posicoes.setGravidade()
                posicoes.parar()
                posicoes.setReturn()
                tela.novaTela()
            elif(globais.GAME_STATE == 2):
                dificuldade.draw()
                dificuldade.setReturn()
                dificuldade.setReturn()
            elif globais.GAME_STATE == 3:
                pontuacao.setRank()
            janela.update()
    if(teclado.key_pressed("LEFT")):
        globais.STATUS_PERSONAGEM = 3
        posicoes.setUpdate()
        while(globais.STATUS_PERSONAGEM == 3):
            if globais.GAME_STATE == 1:
                tela.getFundo()
                posicoes.getUpdate()
                humano.setPosicao()
                humano.setAtaque()
                humano.setInverter()
                humano.colisao()
                posicoes.setGravidade()
                posicoes.parar()
                posicoes.setReturn()
                tela.novaTela()
            elif(globais.GAME_STATE == 2):
                dificuldade.draw()
                dificuldade.setReturn()
            elif globais.GAME_STATE == 3:
                pontuacao.setRank()
            janela.update()
    if(teclado.key_pressed("UP")):
        if(globais.ESTADO_ANTERIOR % 2 == 0):
            globais.STATUS_PERSONAGEM = 4
            posicoes.setUpdate()
            while(globais.STATUS_PERSONAGEM == 4):
                if globais.GAME_STATE == 1:
                    tela.getFundo()
                    posicoes.getUpdate()
                    humano.setPosicao()
                    humano.setAtaque()
                    humano.setInverter()
                    humano.colisao()
                    posicoes.setGravidade()
                    posicoes.parar()
                    posicoes.setReturn()
                    tela.novaTela()
                elif(globais.GAME_STATE == 2):
                    dificuldade.draw()
                    dificuldade.setReturn()
                elif globais.GAME_STATE == 3:
                    pontuacao.setRank()
                janela.update()
        elif(globais.ESTADO_ANTERIOR % 2 == 1):
            globais.STATUS_PERSONAGEM = 5
            posicoes.setUpdate()
            while(globais.STATUS_PERSONAGEM == 5):
                if globais.GAME_STATE == 1:
                    tela.getFundo()
                    posicoes.getUpdate()
                    humano.setPosicao()
                    humano.setAtaque()
                    humano.setInverter()
                    humano.colisao()
                    posicoes.setGravidade()
                    posicoes.parar()
                    posicoes.setReturn()
                    tela.novaTela()
                elif(globais.GAME_STATE == 2):
                    dificuldade.draw()
                    dificuldade.setReturn()
                elif globais.GAME_STATE == 3:
                    pontuacao.setRank()
                janela.update()
    if(teclado.key_pressed("SPACE")):
        if(globais.ESTADO_ANTERIOR % 2 == 0):
            globais.STATUS_PERSONAGEM = 6
            posicoes.setUpdate()
            while(globais.STATUS_PERSONAGEM == 6):
                if globais.GAME_STATE == 1:
                    tela.getFundo()
                    posicoes.getUpdate()
                    humano.setPosicao()
                    humano.setAtaque()
                    humano.setInverter()
                    humano.colisao()
                    posicoes.setGravidade()
                    posicoes.parar()
                    posicoes.setReturn()
                    tela.novaTela()
                elif(globais.GAME_STATE == 2):
                    dificuldade.draw()
                    dificuldade.setReturn()
                elif globais.GAME_STATE == 3:
                    pontuacao.setRank()
                janela.update()
        elif(globais.ESTADO_ANTERIOR % 2 == 1):
            globais.STATUS_PERSONAGEM = 7
            posicoes.setUpdate()
            while(globais.STATUS_PERSONAGEM == 7):
                if globais.GAME_STATE == 1:
                    tela.getFundo()
                    posicoes.getUpdate()
                    humano.setPosicao()
                    humano.setAtaque()
                    humano.setInverter()
                    humano.colisao()
                    posicoes.setGravidade()
                    posicoes.parar()
                    posicoes.setReturn()
                    tela.novaTela()
                elif(globais.GAME_STATE == 2):
                    dificuldade.draw()
                    dificuldade.setReturn()
                elif globais.GAME_STATE == 3:
                    pontuacao.setRank()
                janela.update() 
    if(teclado.key_pressed("DOWN")):
        if(globais.ESTADO_ANTERIOR % 2 == 0):
            globais.STATUS_PERSONAGEM = 8
            posicoes.setUpdate()
        elif(globais.ESTADO_ANTERIOR % 2 == 1):
            globais.STATUS_PERSONAGEM = 9
            posicoes.setUpdate()

    if(globais.GAME_STATE == 0):
        menu.draw()
        menu.getMenu()
    elif globais.GAME_STATE == 1:
        tela.getFundo()
        posicoes.getUpdate()
        humano.setPosicao()
        humano.setAtaque()
        humano.setInverter()
        humano.colisao()
        posicoes.setGravidade()
        posicoes.parar()
        posicoes.setReturn()
        tela.novaTela()
    elif(globais.GAME_STATE == 2):
            dificuldade.draw()
            dificuldade.setReturn()
    elif globais.GAME_STATE == 3:
        pontuacao.setRank()
        pontuacao.setReturn()

    janela.update()