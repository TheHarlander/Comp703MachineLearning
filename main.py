import pygame
import random
import math

# intialize the pygame
pygame.init()

# Screen/Window
screen = pygame.display.set_mode((800, 850))

# Title and Icon
pygame.display.set_caption("704 Machine Learning")
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load('playercar.png')
playerX = 375
playerY = 750
playerXSpeed = 0

# Obstacle
obstacleImage = pygame.image.load('cone.png')
obstacleX = random.randint(200, 600)
obstacleY = 0
obstacleYSpeed = 0.2

# Score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 26)
textX = 10
textY = 10

# Game Over
gameOverFont = pygame.font.Font('freesansbold.ttf', 64)

# Flavour
roadMarking1X = 400
roadMarking1Y = 0
roadMarking2X = 400
roadMarking2Y = 425
roadMarkingSpeed = 0.2


def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (0, 0, 0))
    screen.blit(score, (x, y))


def gameOverText():
    gameOverText = gameOverFont.render("Score: " + str(scoreValue), True, (0, 0, 0))
    screen.blit(gameOverText, (280, 300))


def player(x, y):
    screen.blit(playerImage, (x, y))


def obstacle(x, y):
    screen.blit(obstacleImage, (x, y))


def isCollision(obstacleX, obstacleY, playerX, playerY):
    distance = math.sqrt((math.pow(obstacleX - playerX, 2)) + (math.pow(obstacleY - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # Draw background, grass , barriers and road markings
    screen.fill((75, 75, 75))
    pygame.draw.rect(screen, (100, 140, 100), [0, 0, 150, 850])
    pygame.draw.rect(screen, (30, 30, 30), [140, 0, 10, 850])
    pygame.draw.rect(screen, (100, 140, 100), [650, 0, 200, 850])
    pygame.draw.rect(screen, (30, 30, 30), [650, 0, 10, 850])
    pygame.draw.rect(screen, (200, 200, 200), [roadMarking1X, roadMarking1Y, 20, 100])
    pygame.draw.rect(screen, (200, 200, 200), [roadMarking2X, roadMarking2Y, 20, 100])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXSpeed = -0.3

            if event.key == pygame.K_RIGHT:
                playerXSpeed = 0.3

            # Player Speed up slow down logic
            if event.key == pygame.K_UP:
                obstacleYSpeed += 0.1
                roadMarkingSpeed += 0.1
            if event.key == pygame.K_DOWN:
                obstacleYSpeed -= 0.1
                roadMarkingSpeed -= 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXSpeed = 0

    playerX += playerXSpeed

    # Checking for boundaries
    if playerX <= 100:
        playerX = 100
    elif playerX > 640:
        playerX = 640

    # Obstacle movement + respawn
    obstacleY += obstacleYSpeed

    if obstacleY >= 850:
        obstacleY = -50
        obstacleX = random.randint(175, 625)
        scoreValue += 1
    if scoreValue == 10:
        print("10 score met spawn new obstacle")

    # Road markings + respawn
    roadMarking1Y += roadMarkingSpeed
    roadMarking2Y += roadMarkingSpeed
    if roadMarking1Y >= 850:
        roadMarking1Y = -50
        roadMarking1X = 400
    if roadMarking2Y >= 850:
        roadMarking2Y = -50
        roadMarking2X = 400

    # Collision/ Game over
    collision = isCollision(obstacleX, obstacleY, playerX, playerY)
    if collision:
        obstacleYSpeed = 0
        playerXSpeed = 0
        roadMarkingSpeed = 0
        gameOverText()

    player(playerX, playerY)
    obstacle(obstacleX, obstacleY)
    showScore(textX, textY)
    pygame.display.update()
