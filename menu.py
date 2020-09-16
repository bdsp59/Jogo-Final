from PPlay.window import *
from PPlay.gameimage import *
import globais

class Menu(object):
    def __init__(self, window):
        self.window = window
        self.mouse = Window.get_mouse()
        self.setMenu()

    def draw(self):
        self.fundomenu.draw()
        self.play.draw()
        self.dificuldades.draw()
        self.ranking.draw()
        self.quit.draw()

    def setMenu(self):
        self.fundomenu = GameImage("img/fundomenu_ninja.jpg")
        self.play = GameImage("img/start.png")
        self.dificuldades = GameImage("img/difficulty.png")
        self.quit = GameImage("img/quit.png")
        self.ranking = GameImage("img/highscore.png")

        self.play.x = self.window.width/6 - self.play.width/2
        self.play.y = self.window.height/3 - self.play.height/2
        self.dificuldades.x = self.play.x
        self.dificuldades.y = self.play.y + self.play.height
        self.ranking.x = self.play.x
        self.ranking.y = self.dificuldades.y + self.dificuldades.height
        self.quit.x = self.play.x
        self.quit.y = self.ranking.y + self.ranking.height

    def getMenu(self):
        if self.mouse.is_over_object(self.play) and self.mouse.is_button_pressed(1):
            globais.GAME_STATE = 1
        if self.mouse.is_over_object(self.dificuldades) and self.mouse.is_button_pressed(1):
            globais.GAME_STATE = 2
        if self.mouse.is_over_object(self.ranking) and self.mouse.is_button_pressed(1):
            globais.GAME_STATE = 3
        if self.mouse.is_over_object(self.quit) and self.mouse.is_button_pressed(1):
            self.window.close()
                