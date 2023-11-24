import pygame;


pygame.init()

screen  = pygame.display.set_mode((800,600))

background = pygame.image.load('background.png')

running = True
while running :

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()