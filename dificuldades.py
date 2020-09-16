from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import Mouse
from tela import Tela
import globais
from PPlay.window import Window
from PPlay.keyboard import Keyboard

class Dificuldade(object):
    def __init__(self):
        self.window = Window(globais.WIDTH, globais.HEIGHT)
        self.mouse = Mouse()
        self.teclado = Keyboard()
        self.tela = Tela(window)

    def setDificuldade(self):
        self.facil = GameImage("img/easy1.png")
        self.medio = GameImage("img/medium1.png")
        self.dificil = GameImage("img/hard1.png")
        self.fundoDificuldade = GameImage("img/fundomenu_ninja.jpg")

        self.facil.x = self.window.width/2 - self.facil.width/2
        self.facil.y = self.window.height/4 - self.facil.height/2
        self.medio.x = self.facil.x
        self.medio.y = self.facil.y + self.facil.height
        self.dificil.x = self.facil.x
        self.dificil.y = self.medio.y + self.medio.height

    def getDificuldade(self):
        if self.mouse.is_over_object(self.facil) and self.mouse.is_button_pressed(1):
            globais.DIFICULDADE = 0
            globais.VEL_INIMIGO_H = -100
        if self.mouse.is_over_object(self.medio) and self.mouse.is_button_pressed(1):
            globais.DIFICULDADE = 1
            globais.VEL_INIMIGO_H = -200
        if self.mouse.is_over_object(self.dificil) and self.mouse.is_button_pressed(1):
            globais.DIFICULDADE = 2
            globais.VEL_INIMIGO_H = -300


    def draw(self):
        self.fundoDificuldade.draw()
        self.facil.draw()
        self.medio.draw()
        self.dificil.draw()

    def setReturn(self):
        if(self.teclado.key_pressed("ESC") or self.mouse.is_button_pressed(1) == True):
            globais.GAME_STATE = 0
        self.window.delay(10)