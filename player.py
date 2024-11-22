import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class CircleShape:
    """Base class representing a circular shape."""
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        """Default draw method (can be overridden)."""
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)


class Player(CircleShape, pygame.sprite.Sprite):
    """Player class inheriting from CircleShape and Sprite."""
    containers = ()  # Class variable to hold sprite groups

    def __init__(self, x, y):
        # Initialize both parent classes
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        # Add this instance to the specified groups
        for group in self.containers:
            group.add(self)

        # Placeholder image and rect for compatibility with pygame.sprite.Sprite
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

        self.rotation = 0  # Initialize rotation to 0

    def triangle(self):
        """Calculates the points of the player's triangle."""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draws the player as a triangle."""
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        """Rotates the player based on delta time."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        """Updates the player's state based on input."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left (invert dt)
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_w]: 
            self.move(-dt) # move forward
        if keys[pygame.K_s]:
            self.move(dt) # move backward

        # Update the rect to keep it synced with the position
        self.rect.center = self.position
