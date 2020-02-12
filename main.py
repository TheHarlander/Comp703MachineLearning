import pygame


pygame.init()

screen = pygame.display.set_mode((500,1000))

class player:
    def __init__(self, sizeX = 50, sizeY = 50, speed = 10):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.speed = speed


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.sizeX -= player.speed
    if keys[pygame.K_RIGHT]:
        player.sizeY -= player.speed

        pygame.draw.rect(screen, (255,0,0), (player.sizeX, player.sizeY, ))
        pygame.display.update()

pygame.quit()