# -*- coding: utf-8 -*-
from PPlay.window import Window
from personagem import Personagem
from tela import Tela
import globais

janela = Window(globais.WIDTH,globais.HEIGHT)

tela = Tela(janela)

personagem = Personagem(janela)
personagem.setPersonagem()

personagem.setPersonagemPosicaoInicial()

while True:
    tela.setTela()

    personagem.setPersonagem()
    personagem.setDraw()

    janela.update()