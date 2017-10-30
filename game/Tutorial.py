import os
from os import path
from settings import *
import pygame

def tutorial():
    img_dir = path.join(game_folder, "img")

    clock = pygame.time.Clock()

    GameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    tuto = pygame.image.load(os.path.join(img_dir, "tutori.jpg")).convert()
    tuto = pygame.transform.scale(tuto, (WIDTH, HEIGHT))
    tuto_rect = tuto.get_rect()


    done = False

    while not done:

        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        GameDisplay.fill(WHITE)
        GameDisplay.blit(tuto, tuto_rect)

        pygame.display.update()
