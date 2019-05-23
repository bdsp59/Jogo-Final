import globais
from PPlay.animation import Animation
from PPlay.keyboard import Keyboard
from tela import Tela

class Personagem(object):
    def __init__(self,window):
        self.window = window
        self.setPersonagemD()
        self.setPersonagemE()
        self.setPersonagemAtaqueD()
        self.setPersonagemAtaqueE()
        self.setPersonagemPuloD()
        self.setPersonagemPuloE()
        self.personagem = self.personagem_d
        self.teclado = Keyboard()
        self.cronometroA = 0
        self.cronometroP = 0

    def setPersonagem(self):
        globais.WIDTH_P = self.personagem.width
        globais.HEIGHT_P = self.personagem.height
        self.setPersonagemPosicao()
        self.personagem.set_position(globais.POS_X, globais.POS_Y)
        if(self.teclado.key_pressed("RIGHT")):
            self.personagem = self.personagem_d
            globais.POS_X += globais.VEL_PERSONAGEM * self.window.delta_time()
            self.personagem.update()

        if(self.teclado.key_pressed("LEFT") and (self.personagem.x > 0)):
            self.personagem = self.personagem_e
            globais.POS_X -= globais.VEL_PERSONAGEM * self.window.delta_time()
            self.personagem.update()

        if(self.teclado.key_pressed("SPACE")):
            if(self.cronometroA <=0):
                if(self.personagem == self.personagem_d):
                    self.getPersonagemAtaqueD()
                if(self.personagem == self.personagem_e):
                    self.getPersonagemAtaqueE()
                self.cronometroA = globais.RECARGA
                self.personagem.update()
        self.cronometroA -= 1

        if(self.teclado.key_pressed("UP")):
            if(self.cronometroP <= 0):
                while (globais.POS_Y > self.window.height - (2.5*self.personagem.height) - globais.HEIGHT_S):
                    globais.POS_Y -= globais.PULO_PERSONAGEM*self.window.delta_time()
                self.cronometroP = globais.RECARGA
            self.cronometroP -= 1
        self.setGravidade()

    def setPersonagemPosicaoInicial(self):
        globais.POS_X = 0
        globais.POS_Y = self.window.height - self.personagem.height - globais.HEIGHT_S

    def setPersonagemPosicao(self):
        if(self.personagem.y + self.personagem.height > self.window.height - globais.HEIGHT_S):
            globais.POS_Y = self.window.height - self.personagem.height - globais.HEIGHT_S

    def setGravidade(self):
        if(globais.POS_Y < self.window.height - self.personagem.height - globais.HEIGHT_S):
            globais.POS_Y += globais.GRAVIDADE *self.window.delta_time()

    def setPersonagemD(self):
        self.personagem_d = Animation("img/personagem_d.png", 4, loop=True)
        self.personagem_d.set_sequence_time(0, 4, 100, loop = True)

    def setPersonagemE(self):
        self.personagem_e = Animation("img/personagem_e.png", 4, loop=True)
        self.personagem_e.set_sequence_time(0, 4, 100, loop = True)

    def setPersonagemPuloD(self):
        self.personagem_pulo_d = Animation("img/pulo_d.png", 3, loop = True)
        self.personagem_pulo_d.set_sequence_time(0, 3, 100, loop = True)

    def setPersonagemPuloE(self):
        self.personagem_pulo_e = Animation("img/pulo_e.png", 3, loop = True)
        self.personagem_pulo_e.set_sequence_time(0, 3, 100, loop = True)

    def setPersonagemAtaqueD(self):
        self.personagem_ataque_d = Animation("img/ataque_d.png", 6, loop = True)
        self.personagem_ataque_d.set_sequence_time(0, 6, 36, loop = True)

    def setPersonagemAtaqueE(self):
        self.personagem_ataque_e = Animation("img/ataque_e.png", 6, loop = True)
        self.personagem_ataque_e.set_sequence_time(0, 6, 50, loop = True)

    def getPersonagemAtaqueD(self):
        self.personagem = self.personagem_ataque_d
        self.personagem.update()

    def getPersonagemAtaqueE(self):
        self.personagem = self.personagem_ataque_e
        self.personagem.update()

    def getPersonagemPuloD(self):
        self.personagem = self.personagem_pulo_d
        self.personagem.update()

    def getPersonagemPuloE(self):
        self.personagem = self.personagem_pulo_e
        self.personagem.update()

    def setDraw(self):
        self.setPersonagem()
        self.personagem.draw()