#!/usr/bin/env python3

import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    numpass, numfail = pygame.init()
    print(f"{numpass} modules passed initialization, {numfail} modules failed")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameloop(screen)


def gameloop(screen):
    clock = pygame.time.Clock()
    # In seconds
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        # Reset screen
        screen.fill(color=(0, 0, 0))

        # Logic
        player.update(dt)

        # Draw
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
