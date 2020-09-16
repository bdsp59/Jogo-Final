import globais
from PPlay.gameimage import GameImage
from PPlay.animation import Animation

class Tela(object):
    def __init__(self,window):
        self.window = window
        #self.setFundo()
        self.setSolo()
        self.fundo =[]
    
    def setTela(self):
        self.window.set_title("Ninja's Life")

    def setTelaRank(self):
        self.fundo = GameImage("img/fundo_rank.png")
        self.fundo.draw()
        self.window.set_title("Ninja's Life")

    def setTelaDificuldade(self):
        self.fundo = GameImage("img/fundo_1.png")
        self.fundo.draw()
        self.window.set_title("Ninja's Life")

    def setFundo(self):
        self.fundo_atual = Animation("img/Fundo_1.png", 1, loop = False)
        self.fundo.append(self.fundo_atual)

    def getFundo(self):
        self.fundo[globais.FUNDO_ATUAL].draw()
        self.solo_0.draw()

    def setSolo(self):
        self.solo_0 = Animation("img/chao_1.png", 4, loop = False)
        self.solo_0.set_position(-10, globais.HEIGHT - self.solo_0.height)
        globais.HEIGHT_S = self.solo_0.height

    def getSolo(self):
        return self.solo_0

    def novaTela(self):
        if(globais.POS_X + globais.WIDTH_P> globais.WIDTH):
            self.setFundo()
            globais.FUNDO_ATUAL += 1     
            globais.POS_X = 0