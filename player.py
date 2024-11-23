import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape, pygame.sprite.Sprite):
    """Player class inheriting from CircleShape and Sprite."""
    containers = ()  # Class variable to hold sprite groups

    def __init__(self, x, y):
        # Initialize parent classes
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        # Add this instance to specified groups
        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:
                group.add(self)

        # Set up sprite image and rect
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)

        self.rotation = 0  # Initial rotation

    def triangle(self):
        """Calculate the points of the player's triangle."""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(90) * (self.radius / 1.5)
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player as a triangle."""
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, direction, dt):
        """Rotate the player."""
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Move the player forward."""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        """Update the player's state based on input."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-1, dt)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(1, dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)

        # Sync rect position with actual position
        self.rect.center = self.position
