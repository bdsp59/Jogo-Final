from PPlay.sprite import Sprite
from PPlay.animation import Animation
from PPlay.window import Window
from posicoesTeste import Posicoes
from PPlay.keyboard import Keyboard
import globais

janela = Window(800,600)
janela.set_title('teste')
janela.set_background_color((0,0,0))
posicoes = Posicoes(janela)
teclado = Keyboard()
posicoes.setUpdate()

while(True):
    janela.set_background_color((0,0,0))

    if(teclado.key_pressed("UP")):
        globais.STATUS_PERSONAGEM = 4

    posicoes.getUpdate()

    janela.update()