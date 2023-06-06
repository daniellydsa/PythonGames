import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()
tela = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong")
gameover = False

fundo = pygame.Surface((640,480))
fundo = fundo.convert()
fundo.fill((0,0,0))

barra = pygame.Surface((10,50))
barra1 = barra.convert()
barra1.fill((0,0,255))
barra2 = barra.convert()
barra2.fill((255,0,0))

bolaSur = pygame.Surface((15,15))
circulo = pygame.draw.circle(bolaSur, (0,255,0), (15/2,15/2), 15/2)
bola = bolaSur.convert()

barra1_x, barra2_x = 10,620
barra1_y, barra2_y = 215, 215

bola_x, bola_y = 307.5, 232.5
barra1_mov = barra2_mov = 0
velocidade_x = velocidade_y = velocidade_bola = 250
barra1_pontos = barra2_pontos = 0
velocidade = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

while gameover==False:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameover = True
        if event.type == KEYDOWN:
            if event.key == K_UP:
                barra1_mov = -velocidade
            elif event.key == K_DOWN:
                barra1_mov = velocidade
        elif event.type == KEYUP:
            if event.key == K_UP:
                barra1_mov = 0
            elif event.key == K_DOWN:
                barra1_mov = 0

    pontos1 = font.render(str(barra1_pontos), True, (255,255,255))
    pontos2 = font.render(str(barra2_pontos), True, (255,255,255))

    tela.blit(fundo, (0,0))
    pygame.draw.rect(tela,(255,255,255), Rect((5,5),(630,470)),2)
    pygame.draw.aaline(tela,(255,255,255),(330,5),(330,475))
    tela.blit(barra1, (barra1_x,barra1_y))
    tela.blit(barra2, (barra2_x,barra2_y))
    tela.blit(bola,(bola_x,bola_y))
    tela.blit(pontos1, (250,210))
    tela.blit(pontos2, (380,210))

    barra1_y += barra1_mov
    tempo = clock.tick(50)
    tempo_segs = tempo/1000.0
    bola_x += velocidade_x * tempo_segs
    bola_y += velocidade_y * tempo_segs
    velocidade = velocidade_bola * tempo_segs

    if bola_x >= 305:
        if not barra2_y == bola_y + 7.5:
            if barra2_y < bola_y + 7.5:
                barra2_y += velocidade
            if barra2_y > bola_y - 42.5:
                barra2_y -= velocidade
        else:
            barra2_y == bola_y + 7.5

    if barra1_y >= 420:
        barra1_y = 420
    elif barra1_y <= 10:
        barra1_y = 10
    if barra2_y >= 420:
        barra2_y = 420
    elif barra2_y <= 10:
        barra2_y = 10

    if bola_x <= barra1_x + 10:
        if (bola_y >= barra1_y - 7.5 and 
        bola_y <= barra1_y + 42.5):
            bola_x = 20
            velocidade_x = -velocidade_x
    if bola_x >= barra2_x - 15:
        if (bola_y >= barra2_y - 7.5 and
        bola_y <= barra2_y + 42.5):
            bola_x = 605
            velocidade_x = -velocidade_x
    
    if bola_x < 5:
        barra2_pontos +=1
        bola_x, bola_y = 320, 232.5
        barra1_y, barra2_y = 215, 215
    elif bola_x > 620:
        barra1_pontos += 1
        bola_x, bola_y = 307.5, 232.5
        barra1_y, barra2_y = 215, 215

    if bola_y <= 10:
        velocidade_y = -velocidade_y
        bola_y = 10
    elif bola_y >= 457.5:
        velocidade_y = -velocidade_y
        bola_y = 457.5
        
    pygame.display.flip()