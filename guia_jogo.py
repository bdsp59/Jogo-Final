'''
O jogo deve ser capaz de apresentar o personagem, inimigos, plataformas e chão. Para cada um dos elementos anteriormente teremos que ter uma classe especifica,
cada uma com um respectivo arquivo py, aonde serão desenvolvidos o que cada GameObject do jogo deve fazer. Além de que seram necessários um arquivo py que deve
conter os valores globais, que serão valores padrões usados ao longo do jogo, e um arquivo main.py que ficará responsável por chamar todos as classes no movimento
certo, inicializar a janela do jogo e fazer ele rodar.

Vamos agora detalhar o que deve estar contido em cada um desses arquivos:

1 - O personagem:
    Nesse arquivo teremos uma classe Personagem que será responsável por criar animações dos movimentos do personagem e criar funções para o que deve acontecer
    quando ele realizar algum desses movimentos. Esses movimentos consistem em:
        1.1 - Andar para a esquerda e direita atráves do comando, dado pelas setas do teclado, que o usuário irá passar
        1.2 - Realizar saltos, que deveram ter limitadores de modo que o jogador não possa pular eternamente, e algo que o faça voltar ao solo
            if (self.teclado.key_pressed("UP")):
                if(self.personagem = self.personagem_d):
                self.personagem = self.personagem_pulo_d
                aux = globais.POS_Y - globais.PULO_PERSONAGEM
                while aux < globais.POS_Y:
                    globais.POS_Y -= globais.VEL_PERSONAGEM * self.window.delta_time()
        1.3 - Realizar ataques, tanto a direita quanto a esquerda, de modo que possa atacar inimigos dos dois lados


    Criar uma classe ou função para cada estado de ação do personagem:
        0-Parado
        1-Ataque
        2-Pulo
        3-Abaixado
        4-Kunai

    Criar uma variavel global para capturar o estado atual e possa ser alterada para um novo estado
        PERSONAGEM_STATE

    Entrega dia 05/07:
        código pendrive professor
        trazer impresso: GDD atualizado, com todas as alterções e um manual de jogo(explicar como joga) - ENTREGAR NO MOMENTO QUE FOR APRESENTAR O JOGO!!!!!!
        Jogo deve estar jogável e com a mesma função apresentada no gdd original
'''