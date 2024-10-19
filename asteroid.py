#!/usr/bin/env python3

from circleshape import CircleShape
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_SPLIT_ACCELERATION,
)
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Any other asteroid
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.copy().rotate(angle) * ASTEROID_SPLIT_ACCELERATION
        velocity2 = self.velocity.rotate(-angle) * ASTEROID_SPLIT_ACCELERATION
        radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position.x, self.position.y
        asteroid1 = Asteroid(x, y, radius)
        asteroid2 = Asteroid(x, y, radius)
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
