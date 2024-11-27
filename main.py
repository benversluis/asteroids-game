import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids with Lives and Respawning")
    clock = pygame.time.Clock()

    # Initialize font for score and lives display
    font = pygame.font.Font(None, 36)

    # Initialize game variables
    score = 0
    lives = 3
    respawn_time = 3  # Seconds of invulnerability after respawn
    player_invulnerable = False
    invulnerability_timer = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update game objects
        for obj in updatable:
            obj.update(dt)

        # Handle collisions
        if not player_invulnerable:
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    lives -= 1
                    if lives <= 0:
                        print("Game over!")
                        sys.exit()

                    # Respawn player
                    player.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    player_invulnerable = True
                    invulnerability_timer = pygame.time.get_ticks()  # Start invulnerability timer

        # Handle invulnerability timer
        if player_invulnerable:
            if pygame.time.get_ticks() - invulnerability_timer > respawn_time * 1000:
                player_invulnerable = False

        # Check asteroid collisions with shots
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 10

        # Draw everything
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        # Display lives
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
