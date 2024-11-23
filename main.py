import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()

# Screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids Game")

# Clock and delta time initialization
clock = pygame.time.Clock()
dt = 0

# Create groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()

# Add the Player class to both groups
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids_group, updatable, drawable)
AsteroidField.containers = (updatable)

# Instantiate the player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

asteroids = [
    Asteroid(100, 100, 30),
    Asteroid(300, 200, 40),
    Asteroid(500, 400, 50)
]

asteroid_field = AsteroidField(10, SCREEN_WIDTH, SCREEN_HEIGHT)

for asteroid in asteroids:
    asteroids_group.add(asteroid)
    updatable.add(asteroid)
    drawable.add(asteroid)

# Game loop
while True:
    # Handle events (exit condition)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update and draw all updatable objects
    screen.fill((0, 0, 0))  # Fill the screen with black
    for obj in updatable:
        obj.update(dt)
        obj.draw(screen)

    # Check for collisions between player and asteroids
    if pygame.sprite.spritecollide(player, asteroids_group, False, pygame.sprite.collide_circle):
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Refresh the screen
    pygame.display.flip()

    # Control the frame rate and calculate delta time
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds