import pygame
from sys import exit
import random


DINO_IMAGE = pygame.transform.scale(pygame.image.load("dino.png"), (88, 94))


GAME_WIDTH = 750
GAME_HEIGHT = 250

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Dino Bams")
clock = pygame.time.Clock()

dino = pygame.Rect((50, 50), DINO_IMAGE.get_size())

def draw():
    window.blit(DINO_IMAGE, dino)

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    draw()
    pygame.display.update()
    clock.tick(60)