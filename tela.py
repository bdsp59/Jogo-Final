import globais
from PPlay.gameimage import GameImage
from PPlay.animation import Animation

class Tela(object):
    def __init__(self,window):
        self.window = window
        self.setFundo()
        self.setSolo()

    def setTela(self):
        self.window.set_title("Ninja's Life")
        self.fundo_0.draw()
        self.solo_0.draw()
    
    def setFundo(self):
        if (globais.FUNDO_ATUAL == 0):
            self.fundo_0 = GameImage("img/fundo_1v2.png")
            self.fundo_atual = Animation("img/fundo_1v2.png", 4, loop = False)

    def setSolo(self):
        self.solo_0 = Animation("img/chao_1.png", 4, loop = False)
        if(globais.TELA_ATUAL == 0):
            self.solo_0.set_position(-10, globais.HEIGHT - self.solo_0.height)
            
        globais.HEIGHT_S = self.solo_0.height

