#!/usr/bin/env python3

import pygame

from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot


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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        # Reset screen
        screen.fill(color=(0, 0, 0))

        # Logic
        for sprite in updatable:
            sprite.update(dt)

        # Collision checks
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

            if player.collision(asteroid):
                print("Game over!")
                return

        # Draw
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
