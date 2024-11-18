import pygame
import sys

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()

    print("Starting asteroids!")
    print("Screen width: " f"{SCREEN_WIDTH}")
    print ("Screen height: " f"{SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()