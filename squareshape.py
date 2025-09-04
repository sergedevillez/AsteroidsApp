import pygame

# Base class for game objects
class SquareShape(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.position.x, self.position.y, self.size, self.size), 2)

    def update(self, dt):
        # sub-classes must override
        pass