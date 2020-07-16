import pygame

pygame.init()

BACKGROUND = pygame.image.load("imagens/fundo.png")
CAR = pygame.image.load("imagens/carro.png")

car_x = 450
car_y = 230
speed = 8


window_x = 1000
window_y = 800
WINDOW = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Game")

loop = True
while loop:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        car_y -= speed
    if key[pygame.K_DOWN]:
        car_y += speed
    if key[pygame.K_LEFT]:
        car_x -= speed
    if key[pygame.K_RIGHT]:
        car_x += speed
                
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.transform.scale(BACKGROUND, (1000, 800), WINDOW)
    WINDOW.blit(CAR, (car_x, car_y))
    
    pygame.display.update()

