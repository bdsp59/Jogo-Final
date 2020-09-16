import globais
from PPlay.animation import *
from PPlay.collision import Collision
from tela import Tela
from posicoes import Posicoes
import random

class Humano(object):
    def __init__(self, window):
        self.window = window
        self.tela = Tela(window)
        self.collision = Collision()
        self.setHumanoE()
        self.setHumanoD()
        self.setAtaqueHumanoD()
        self.setAtaqueHumanoE()
        self.humano = self.humano_e
        self.humanoVetor = []
        self.setPosicaoInicial()
        self.posicoes = Posicoes(window)
        self.random = random.SystemRandom()

    def setPosicaoInicial(self):
        globais.HUMANO_POS_X = globais.WIDTH - 200
        globais.HUMANO_POS_Y = (globais.HEIGHT - globais.HEIGHT_S - self.humano.height)
        self.humano.set_position(globais.HUMANO_POS_X, globais.HUMANO_POS_Y)
        self.humanoVetor.append(self.humano)

    def setPosicao(self):
        globais.HUMANO_POS_X += globais.VEL_INIMIGO_H*self.window.delta_time()
        self.humanoVetor[0].set_position(globais.HUMANO_POS_X, globais.HUMANO_POS_Y)
        self.humanoVetor[0].update()
        self.humanoVetor[0].draw()

    def setHumanoD(self):
        self.humano_d = Animation("img/inimigo_d2.png", 6, loop = True)
        self.humano_d.set_sequence_time(0, 6, 600, loop = True)

    def setHumanoE(self):
        self.humano_e = Animation("img/inimigo_e2.png", 6, loop = True)
        self.humano_e.set_sequence_time(0, 6, 600, loop = True)

    def setAtaqueHumanoD(self):
        self.ataque_humano_d = Animation("img/Inimigo_atk_d.png", 4, loop=True)
        self.ataque_humano_d.set_sequence_time(0, 4, 200, loop=True)

    def setAtaqueHumanoE(self):
        self.ataque_humano_e = Animation("img/Inimigo_atk_e.png", 4, loop=True)
        self.ataque_humano_e.set_sequence_time(0, 4, 200, loop=True)

    def setAtaque(self):
        if((self.humanoVetor[0].x + self.humanoVetor[0].width < globais.POS_X - 30) and (self.humanoVetor[0].x + self.humanoVetor[0].width < globais.POS_X) and (self.humanoVetor[0] == self.humano_d) and (self.humanoVetor[0].y <= globais.POS_Y + globais.HEIGHT_P)):
            return True
        elif((self.humanoVetor[0].x < globais.POS_X + globais.WIDTH_P + 30) and (self.humanoVetor[0].x > globais.POS_X + globais.WIDTH_P) and (self.humanoVetor[0] == self.humano_e) and (self.humanoVetor[0].y <= globais.POS_Y + globais.HEIGHT_P)):
            return True
        return False

    def setGravidade(self):
        if(globais.POS_Y < self.window.height):
            if((self.collision.collided(self.humano, self.tela.getSolo())) == False):
                globais.POS_Y += globais.GRAVIDADE * self.window.delta_time()

    def setInverter(self):
        if(self.setAtaque() == False):
            if(self.humanoVetor[0].x + self.humanoVetor[0].width + 50 < globais.POS_X):
                globais.VEL_INIMIGO_H = 100
                self.humanoVetor[0] = self.humano_d
            elif(self.humanoVetor[0].x > globais.POS_X + globais.WIDTH_P + 50):
                globais.VEL_INIMIGO_H = -100
                self.humanoVetor[0] = self.humano_e
        elif(self.setAtaque() == True):
            if(globais.VEL_INIMIGO_H == -100):
                self.humanoVetor[0] = self.ataque_humano_e
            elif(globais.VEL_INIMIGO_H == 100):
                self.humanoVetor[0] = self.ataque_humano_d

    def colisao(self):
        self.personagem = self.posicoes.getPersonagem()
        if(self.collision.collided(self.personagem, self.humanoVetor[0]) == True):
            if(self.collision.collided(self.personagem, self.humanoVetor[0]) and (self.humano == self.ataque_humano_d or self.humano == self.ataque_humano_e)):
                self.posicoes.setPosicaoInicial()
                globais.VIDA_P -= 1
            elif(self.collision.collided(self.personagem, self.humanoVetor[0]) and (globais.STATUS_PERSONAGEM == 6 or globais.STATUS_PERSONAGEM == 7)):
                self.humanoVetor.pop(0)
                self.setPosicaoInicial()
                globais.PONTUACAO += 10

