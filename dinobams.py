import pygame
from sys import exit
import random


GAME_WIDTH = 750
GAME_HEIGHT = 250

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Dino Bams")
clock = pygame.time.Clock()


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)