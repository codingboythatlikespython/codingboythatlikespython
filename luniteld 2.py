import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")

game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)




while True:
    for event in pyagme.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    clock.tick(120)
    pygame.display.update
    