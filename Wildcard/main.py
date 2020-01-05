import pygame
import time

pygame.init()
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption('guessing game')
font = pygame.font.Font("OpenSans-BoldItalic.ttf", 10)

black = (0, 0, 0)
white = (255, 255, 255)
hintText = font.render('a', True, black, white)
textRect = hintText.get_rect()
textRect.center = (200, 200)

carImg = pygame.image.load('lightbulb.png')


def lightbulb():
    gameDisplay.blit(carImg, (0, 0))


crashed = False
while not crashed:
    gameDisplay.blit(hintText, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    lightbulb()
    pygame.display.update()

pygame.quit()
quit()
