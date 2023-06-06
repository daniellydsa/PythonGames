import pygame as pg
import random
pg.init()

tela = pg.display.set_mode((600,400))
pg.display.set_caption('Snake')

tempo = pg.time.Clock()
fim_de_jogo = False
x, y, x_acrescimo, y_acrescimo = 100, 100, 0, 0

cobra = []
tamanho = 1
bloco = 10
velocidade_jogo = 20

x_comida = bloco*random.randint(0,600/bloco)
y_comida = bloco*random.randint(0,400/bloco)

tela.fill([0,0,255])

while not fim_de_jogo:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            fim_de_jogo=True
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LEFT:
                x_acrescimo = -bloco
                y_acrescimo = 0
            if event.key==pg.K_RIGHT:
                x_acrescimo = bloco
                y_acrescimo = 0
            if event.key==pg.K_UP:
                x_acrescimo = 0
                y_acrescimo = -bloco
            if event.key==pg.K_DOWN:
                x_acrescimo = 0
                y_acrescimo = bloco
    x += x_acrescimo
    y += y_acrescimo

    tela.fill([0,0,255])
    pg.draw.rect(tela,[140,0,0],[x_comida,y_comida,bloco,bloco])
    cobra.append([x,y])
    if len(cobra) > tamanho:
        del cobra[0]
    for pedaco in cobra:
        pg.draw.rect(tela,[0,0,0], [pedaco[0], pedaco[1], bloco, bloco])
    
    if x_comida == cobra[-1][0] and y_comida == cobra[-1][1]:
        x_comida = bloco*random.randint(0,(600-bloco)/bloco)
        y_comida = bloco*random.randint(0,(400-bloco)/bloco)
        tamanho+=1
    if cobra[-1][0] not in range(0,600-bloco) or cobra[-1][1] not in range(0,400-bloco):
        fim_de_jogo = True

    pg.display.update()
    tempo.tick(velocidade_jogo)
pg.quit()