import pygame
import random

from player import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self)

        self.velocity = pygame.Vector2(
            random.uniform(-100, 100),
            random.uniform(-100, 100)
        )

        for group in self.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt