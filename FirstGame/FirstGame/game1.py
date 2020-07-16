import pygame
from pygame.locals import *
from random import randint

pygame.init()

x = 450
y = 500
pol_x = 270
pol_y = 800
pol1_y = 800
pol2_y = 800

timer = 0
tempo_segundo = 0
speed = 10
speed_others = 5

background = pygame.image.load('fundo.png')
car = pygame.image.load('carro.png')
car_police = pygame.image.load('car_police.png')
car_police1 = pygame.image.load('car_police_2.png')
car_police2 = pygame.image.load('car_police_3.png')


window = pygame.display.set_mode((1000, 705))
pygame.display.set_caption("Primeiro jogo")

font = pygame.font.SysFont('arial Black', 30)
texto = font.render("Time: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = 65, 50

window_open = True

while window_open:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
    
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= speed
    
    if comandos[pygame.K_DOWN]:
        y += speed 

    if comandos[pygame.K_RIGHT] and x < 690:
        x += speed

    if comandos[pygame.K_LEFT] and x> 240:
        x -= speed

    if pol_y <= -60 and pol1_y <= -60 and pol2_y <= -60:
        pol_y = randint(720, 800)
        pol1_y = randint(720, 800)
        pol2_y = randint(720, 800)

    if timer < 50:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Time: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0
    
    pol_y -= speed_others
    pol1_y -= speed_others + 8
    pol2_y -= speed_others + 8

    window.blit(background, (0, 0))
    window.blit(car, (x, y))
    window.blit(car_police, (pol_x, pol_y))
    window.blit(car_police1, (pol_x + 370, pol1_y))
    window.blit(car_police2, (pol_x + 180, pol2_y))
    window.blit(texto, pos_texto)

    pygame.display.update()
    
pygame.quit()




