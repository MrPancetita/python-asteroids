import pygame

# Base class fro game objects

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        #TODO later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = 
        
