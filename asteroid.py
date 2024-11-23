import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Add to groups
        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:
                group.add(self)

        # Initialize velocity
        self.velocity = pygame.Vector2(
            random.uniform(-100, 100),
            random.uniform(-100, 100)
        )

        # Define image and rect for compatibility with pygame.sprite.Sprite
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=(x, y))
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        """Update position and handle screen wrapping."""
        self.position += self.velocity * dt
        self.rect.center = self.position  # Sync rect with position

        # Screen wrapping
        screen_width, screen_height = pygame.display.get_surface().get_size()
        if self.position.x < 0:
            self.position.x = screen_width
        elif self.position.x > screen_width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = screen_height
        elif self.position.y > screen_height:
            self.position.y = 0
