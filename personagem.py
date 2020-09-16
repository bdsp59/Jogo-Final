import globais
from PPlay.animation import Animation
from PPlay.keyboard import Keyboard
from tela import Tela
from posicoes import Posicoes

class Personagem(object):
    def __init__(self,window):
        self.window = window
        self.posicoes = Posicoes(self.window)
        self.teclado = Keyboard()

    def setPersonagem(self):
        