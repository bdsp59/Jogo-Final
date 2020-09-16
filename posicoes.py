from PPlay.sprite import Sprite
from PPlay.animation import Animation
from PPlay.collision import Collision
from PPlay.keyboard import Keyboard
import globais
from tela import Tela
from highscore import Pontuacao

class Posicoes(object):
    def __init__(self, window):
        self.window = window
        self.tela = Tela(window)
        self.collision = Collision()
        self.setParadoD()
        self.personagem = self.parado_d
        globais.POS_Y = (globais.HEIGHT - globais.HEIGHT_S - self.parado_d.height)
        self.setPosicaoInicial()
        self.teclado = Keyboard()
        self.pontuacao = Pontuacao(window)
        self.kunaiD = []
        self.kunaiE = []
        self.cronometro = 0

    def setPosicaoInicial(self):
        self.personagem.set_position(globais.POS_X, globais.POS_Y)
        self.personagem.draw()

    def setPosicao(self):
        self.personagem.set_position(globais.POS_X, globais.POS_Y)
        self.personagem.draw()

    def setParadoD(self):
        self.parado_d = Sprite("img/parado_d2.png")
        self.personagem = self.parado_d

    def setParadoE(self):
        self.parado_e = Sprite("img/parado_e2.png")
        self.personagem = self.parado_e

    def setAndandoD(self):
        self.andando_d = Animation("img/personagem_d2.png", 5, loop = True)
        self.andando_d.set_sequence_time(0, 5, 300, loop = True)
        self.personagem = self.andando_d

    def setAndandoE(self):
        self.andando_e = Animation("img/personagem_e2.png", 5, loop = True)
        self.andando_e.set_sequence_time(0, 5, 300, loop = True)
        self.personagem = self.andando_e

    def setPuloD(self):
        self.pulo_d = Animation("img/pulo_d2.png", 4, loop = True)
        self.pulo_d.set_sequence_time(0, 4, 500, loop = True)
        self.personagem = self.pulo_d

    def setPuloE(self):
        self.pulo_e = Animation("img/pulo_e2.png", 4, loop = True)
        self.pulo_e.set_sequence_time(0, 4, 500, loop = True)
        self.personagem = self.pulo_e

    def setAtaqueD(self):
        self.ataque_d = Animation("img/ataque_d2.png", 7, loop = True)
        self.ataque_d.set_sequence_time(0, 7, 100, loop = True)
        self.personagem = self.ataque_d

    def setAtaqueE(self):
        self.ataque_e = Animation("img/ataque_e2.png", 7, loop = True)
        self.ataque_e.set_sequence_time(0, 7, 100, loop = True)
        self.personagem = self.ataque_e

    def setAbaixadoD(self):
        self.abaixado_d = Sprite("img/abaixado_d.png")
        self.personagem = self.abaixado_d

    def setAbaixadoE(self):
        self.abaixado_e = Sprite("img/abaixado_e.png")
        self.personagem = self.abaixado_e

    def setUpdate(self):
        if(globais.STATUS_PERSONAGEM == 0):
            self.setParadoD()
        elif(globais.STATUS_PERSONAGEM == 1):
            self.setParadoE()
        elif(globais.STATUS_PERSONAGEM == 2):
            self.setAndandoD()
        elif(globais.STATUS_PERSONAGEM == 3):
            self.setAndandoE()
        elif(globais.STATUS_PERSONAGEM == 4):
            self.setPuloD()
        elif(globais.STATUS_PERSONAGEM == 5):
            self.setPuloE()
        elif(globais.STATUS_PERSONAGEM == 6):
            self.setAtaqueD()
        elif(globais.STATUS_PERSONAGEM == 7):
            self.setAtaqueE()
        elif(globais.STATUS_PERSONAGEM == 8):
            self.setAbaixadoD()
        elif(globais.STATUS_PERSONAGEM == 9):
            self.setAbaixadoE()
        elif(globais.STATUS_PERSONAGEM == 10):
            self.setKunaiD()
        elif(globais.STATUS_PERSONAGEM == 11):
            self.setKunaiE()
        globais.WIDTH_P = self.personagem.width
        globais.HEIGHT_P = self.personagem.height

    def getUpdate(self):
        if(globais.POS_X < 0):
            globais.POS_X = 0
        altura = globais.HEIGHT - (3*self.parado_d.height)
        if(globais.STATUS_PERSONAGEM == 0):
            self.setParadoD()
            self.setPosicao()
            globais.ESTADO_ANTERIOR = 0
        elif(globais.STATUS_PERSONAGEM == 1):
            self.setParadoE()
            self.setPosicao()
            globais.ESTADO_ANTERIOR = 1
        elif(globais.STATUS_PERSONAGEM == 2):
            globais.POS_X += globais.VEL_PERSONAGEM * self.window.delta_time()
            self.setPosicao()
            if(self.teclado.key_pressed("UP")):
                globais.STATUS_PERSONAGEM = 4
            if(self.teclado.key_pressed("SPACE")):
                globais.STATUS_PERSONAGEM = 6
            self.personagem.update()
            globais.ESTADO_ANTERIOR = 0
        elif(globais.STATUS_PERSONAGEM == 3):
            globais.POS_X -= globais.VEL_PERSONAGEM * self.window.delta_time()
            self.setPosicao()
            if(self.teclado.key_pressed("UP")):
                globais.STATUS_PERSONAGEM = 5
            if(self.teclado.key_pressed("SPACE")):
                globais.STATUS_PERSONAGEM = 7
            self.personagem.update()
            globais.ESTADO_ANTERIOR = 1
        elif(globais.STATUS_PERSONAGEM == 4):
            self.setPosicao()
            if(globais.POS_Y > altura and self.personagem.get_curr_frame() == 0):
                self.personagem.set_curr_frame(0)
                globais.POS_Y -= globais.PULO_PERSONAGEM * self.window.delta_time()
                if(self.teclado.key_pressed("RIGHT")):
                    globais.POS_X += globais.PULO_PERSONAGEM * self.window.delta_time()
            elif(globais.POS_Y == altura):
                self.personagem.set_curr_frame(1)
                globais.POS_X += 2
            elif(globais.POS_Y < globais.HEIGHT - globais.HEIGHT_S - self.personagem.height):
                self.personagem.set_curr_frame(2)
                globais.POS_Y += globais.PULO_PERSONAGEM * self.window.delta_time()
                if(self.teclado.key_pressed("RIGHT")):
                    globais.POS_X += (globais.PULO_PERSONAGEM * self.window.delta_time())/2
                if(globais.POS_Y-109 >= globais.HEIGHT - 350):
                    globais.STATUS_PERSONAGEM = 1
            globais.ESTADO_ANTERIOR = 0
        elif(globais.STATUS_PERSONAGEM == 5):
            self.setPosicao()
            if(globais.POS_Y > altura and self.personagem.get_curr_frame() == 0):
                self.personagem.set_curr_frame(0)
                globais.POS_Y -= globais.PULO_PERSONAGEM * self.window.delta_time()
                if(self.teclado.key_pressed("LEFT")):
                    globais.POS_X -= globais.PULO_PERSONAGEM * self.window.delta_time()
            elif(globais.POS_Y == altura):
                self.personagem.set_curr_frame(1)
                globais.POS_X += 2
            elif(globais.POS_Y < globais.HEIGHT - globais.HEIGHT_S - self.personagem.height):
                self.personagem.set_curr_frame(2)
                globais.POS_Y += globais.PULO_PERSONAGEM * self.window.delta_time()
                if(self.teclado.key_pressed("LEFT")):
                    globais.POS_X -= (globais.PULO_PERSONAGEM * self.window.delta_time())/2
                if(globais.POS_Y-109 >= globais.HEIGHT - 350):
                    globais.STATUS_PERSONAGEM = 0
            globais.ESTADO_ANTERIOR = 1
        elif(globais.STATUS_PERSONAGEM == 6):
            self.setPosicao()
            self.personagem.update()
            globais.ESTADO_ANTERIOR = 0
        elif(globais.STATUS_PERSONAGEM == 7):
            self.setPosicao()
            self.personagem.update()
            globais.ESTADO_ANTERIOR = 1
        elif(globais.STATUS_PERSONAGEM == 8):
            globais.POS_Y = globais.HEIGHT - self.tela.getSolo().height - self.abaixado_d.height
            self.setPosicao()
            if(self.teclado.key_pressed("DOWN") == False):
                (globais.POS_Y) = (globais.HEIGHT - globais.HEIGHT_S)
                globais.STATUS_PERSONAGEM = 0
            globais.ESTADO_ANTERIOR = 0
        elif(globais.STATUS_PERSONAGEM == 9):
            globais.POS_Y = globais.HEIGHT - self.tela.getSolo().height - self.abaixado_e.height
            self.setPosicao()
            if(self.teclado.key_pressed("DOWN") == False):
                globais.POS_Y = (globais.HEIGHT - globais.HEIGHT_S)
                globais.STATUS_PERSONAGEM = 1
        elif(globais.STATUS_PERSONAGEM == 10):
            self.setPosicao()
            self.personagem.update()
            if (self.cronometro <= 0):
                self.setKunai_D()
                self.cronometro = globais.RECARGA
            self.cronometro -= 1
            globais.ESTADO_ANTERIOR = 0
        elif(globais.STATUS_PERSONAGEM == 11):
            self.setPosicao()
            self.personagem.update()
            if (self.cronometro <= 0):
                self.setKunai_E
                self.cronometro = globais.RECARGA
            self.cronometro -= 1
            globais.ESTADO_ANTERIOR = 1


    def parar(self):
        if((self.personagem.get_curr_frame() == (self.personagem.get_final_frame()-1)) and (globais.ESTADO_ANTERIOR == 0)):
            globais.STATUS_PERSONAGEM = 0
            return False
        elif((self.personagem.get_curr_frame() == (self.personagem.get_final_frame()-1)) and (globais.ESTADO_ANTERIOR == 1)):
            globais.STATUS_PERSONAGEM = 1
            return False
        else:
            return True

    def setGravidade(self):
        if(globais.POS_Y < self.window.height):
            if((self.collision.collided(self.personagem, self.tela.getSolo())) == False):
                globais.POS_Y += globais.GRAVIDADE * self.window.delta_time()

    def getPersonagem(self):
        return self.personagem

    def setReturn(self):
        if(self.teclado.key_pressed("ESC") or (globais.VIDA_PERSONAGEM == 0)):
            self.pontuacao.setArquivoPontuacao()
            globais.GAME_STATE = 0
        self.window.delay(10)