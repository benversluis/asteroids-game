import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, velocity=None):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = velocity or pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius

    # Remove the base draw method or provide a default implementation
    def draw(self, screen):
        # In this case, the base class doesn't draw itself,
        # this should be handled in the subclasses like Player and Asteroid
        pass
