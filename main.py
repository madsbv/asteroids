#!/usr/bin/env python3

import pygame

from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    numpass, numfail = pygame.init()
    print(f"{numpass} modules passed initialization, {numfail} modules failed")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameloop(screen)


def gameloop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
