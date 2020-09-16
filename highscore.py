from PPlay.window import *
from PPlay.gameimage import *
import globais
import os.path
from PPlay.keyboard import Keyboard
from tela import Tela

class Pontuacao(object):
    def __init__(self, window):
        self.window = window
        self.teclado = Keyboard()
        self.tela = Tela(window)

    def setArquivoPontuacao(self):
        self.nome = input("Entre com o nome do jogador: ")
        if(os.path.isfile("Pontuacao.txt") == False):
            self.arquivo = open("Pontuacao.txt", 'w')
        self.arquivo = open("Pontuacao.txt", 'r')
        conteudo = self.arquivo.readlines()
        conteudo.append(self.nome + "\t\t" + str(globais.PONTUACAO))
        conteudo.append("\n")
        self.arquivo = open("Pontuacao.txt", 'w')
        self.arquivo.writelines(conteudo)
        
    def setArquivoCompara(self):
        self.arquivo = open("Pontuacao.txt", 'r')
        valores =[]
        linhas = 0
        conteudo = []
        for line in self.arquivo:
            valores.append(line.split())
            linhas += 1
        for a in range(linhas):
            for i in range((len(valores)-1)):
                for j in range(1,2):
                    if(int(valores[i][j]) < int(valores[i+1][j])):
                        aux = valores[i]
                        valores[i] = valores[i+1]
                        valores[i+1] = aux
        for i in range((len(valores))):
            for j in range(1):
                conteudo.append(str(valores[i][j]) + "\t\t" + str(valores[i][j+1]))
                conteudo.append("\n")
        self.arquivo = open("Pontuacao.txt", 'w')
        self.arquivo.writelines(conteudo)

    def setRank(self):
        self.tela.setTelaRank()
        self.setArquivoCompara()
        valores = []
        conteudo = []
        self.window.draw_text("Melhores Jogadores:", self.window.width/(3.2), self.window.height/4, size = 40, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text("1 - ", 2*(self.window.width/5), self.window.height/2, size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text("2 - ", 2*(self.window.width/5), self.window.height/2 + 30, size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text("3 - ", 2*(self.window.width/5), self.window.height/2 + 60, size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text("4 - ", 2*(self.window.width/5), self.window.height/2 + 90, size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text("5 - ", 2*(self.window.width/5), self.window.height/2 + 120, size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.arquivo = open("Pontuacao.txt", 'r')
        for line in self.arquivo:
            valores.append(line.split())
        if(len(valores)<5):
            for i in range(5 - len(valores)):
                valores.append("-   -")
        linhas = len(valores)
        for i in range(linhas):
            for j in range(1):
                conteudo.append(str(valores[i][j]) + "       " + str(valores[i][j+1]))
        self.window.draw_text(conteudo[0], (2*(self.window.width/5) + 60), (self.window.height/2), size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text(conteudo[1], (2*(self.window.width/5) + 60), (self.window.height/2 + 30), size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text(conteudo[2], (2*(self.window.width/5) + 60), (self.window.height/2 + 60), size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text(conteudo[3], (2*(self.window.width/5) + 60), (self.window.height/2 + 90), size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)
        self.window.draw_text(conteudo[4], (2*(self.window.width/5) + 60), (self.window.height/2 + 120), size = 15, color = (255,255,255), font_name = "Arial", bold = False, italic = False)

    def setReturn(self):
        if(self.teclado.key_pressed("ESC")):
            globais.GAME_STATE = 0
        self.window.delay(10)