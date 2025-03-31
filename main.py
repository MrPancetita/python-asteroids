import pygame
from constants import *  # Importing all constants from the constants module

# This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("BLACK")  # Fill the screen with black color
    pygame.display.flip()  # Update the display to show the filled screen


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game if the quit event is detected
            
if __name__ == "__main__":
    main()
