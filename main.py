import os
import random
import math
import pygame
from os.path import join

pygame.init()

pygame.display.set_caption("Ninja")

WIDTH, HEIGHT = 1000, 800
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)
    return tiles, image


def draw(window, background, bg_image):
    for title in background:
        window.blit(bg_image, title)
    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Yellow.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
