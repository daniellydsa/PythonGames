import pygame, sys, OpenGL, random
from pygame.locals import *
from OpenGL.GL import *

WIDTH = 640
HEIGHT = 480

#variáveis de configuração da bola
xBola = yBola = 0
tamanhoBola = 20
v_xBola = v_yBola = 0.1

#variáveis de configuração do jogador
xJogador = 0
yJogador = -200
tamanhoJogador = 40
v_jogador = 0.25

#variàveis de configuração do inimigo
xInimigo = yInimigo = 0
tamanhoInimigo = 60
v_xInimigo = v_yInimigo = 0.05

def movimento(posicaoAtual, velocidade):
    return posicaoAtual + velocidade

def colisaoY(y,tamanho):
    if(y+tamanho/2 > HEIGHT/2 or
       y-tamanho/2 < -HEIGHT/2):
        return -1
    return 1
def colisaoX(x,tamanho):
    if(x+tamanho/2 > WIDTH/2 or
       x-tamanho/2 < -WIDTH/2):
        return -1
    return 1

def atualizar():
    global xBola,yBola,v_xBola,v_yBola,yJogador,xJogador,xInimigo,yInimigo,v_xInimigo,v_yInimigo, tamanhoJogador, gameOver
    #Movimento da bola
    xBola = movimento(xBola,v_xBola)
    yBola = movimento(yBola,v_yBola)

    #Colisão da bola com as paredes - tranformar em função
    v_yBola *= colisaoY(yBola,tamanhoBola)
    v_xBola *= colisaoX(xBola,tamanhoBola)

    #Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        yJogador = movimento(yJogador, v_jogador)
    if keys[K_s]:
        yJogador = movimento(yJogador, -v_jogador)
    if keys[K_d]:
        xJogador = movimento(xJogador, v_jogador)
    if keys[K_a]:
        xJogador = movimento(xJogador, -v_jogador)
    #Colisão do jogador com a parede
    if(yJogador > HEIGHT/2):
        yJogador = HEIGHT/2
    if(yJogador < -HEIGHT/2):
        yJogador = -HEIGHT/2
    if(xJogador > WIDTH/2):
        xJogador = WIDTH/2
    if(xJogador < -WIDTH/2):
        xJogador = -WIDTH/2
    #Movimento do Inimigo
    xInimigo = movimento(xInimigo, v_xInimigo)
    yInimigo = movimento(yInimigo, v_yInimigo)
    #Colisão do inimigo com a parede
    v_yInimigo *= colisaoY(yInimigo,tamanhoInimigo)
    v_xInimigo *= colisaoX(xInimigo,tamanhoInimigo)

    if(xBola+tamanhoBola/2 > xJogador-tamanhoJogador/2 
    and xBola-tamanhoBola/2 < xJogador+tamanhoJogador/2
    and yBola+tamanhoBola/2 > yJogador-tamanhoJogador/2
    and yBola-tamanhoBola/2 < yJogador+tamanhoJogador/2):
        xBola = random.randrange(-WIDTH/2,WIDTH/2)
        yBola = random.randrange(-HEIGHT/2,HEIGHT/2)
        tamanhoJogador += 10
        if tamanhoJogador >= 300:
            tamanhoJogador = 300

    if(xInimigo+tamanhoInimigo/2 > xJogador-tamanhoJogador/2 
    and xInimigo-tamanhoInimigo/2 < xJogador+tamanhoJogador/2
    and yInimigo+tamanhoInimigo/2 > yJogador-tamanhoJogador/2
    and yInimigo-tamanhoInimigo/2 < yJogador+tamanhoJogador/2):
        tamanhoJogador -= 2
        if tamanhoJogador <= 10:
            gameOver = True

def desenharObjeto(x, y, tamanho, r, g, b):
    glColor3f(r,g,b)
    glBegin(GL_QUADS)
    glVertex2f(-0.5*tamanho+x, -0.5*tamanho+y)
    glVertex2f(0.5*tamanho+x, -0.5*tamanho+y)
    glVertex2f(0.5*tamanho+x, 0.5*tamanho+y)
    glVertex2f(-0.5*tamanho+x, 0.5*tamanho+y)
    glEnd()

def desenhar():
    glViewport(0,0,WIDTH,HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-WIDTH/2, WIDTH/2, -HEIGHT/2, HEIGHT/2, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    desenharObjeto(xBola, yBola, tamanhoBola, 1,1,1)
    desenharObjeto(xJogador, yJogador, tamanhoJogador, 0,1,0)
    desenharObjeto(xInimigo, yInimigo, tamanhoInimigo, 1,0,0)
    pygame.display.flip()

pygame.init()
pygame.display.set_mode((WIDTH,HEIGHT), DOUBLEBUF | OPENGL)
gameOver = False

while not gameOver:
    atualizar()
    desenhar()
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
    pygame.event.pump()
