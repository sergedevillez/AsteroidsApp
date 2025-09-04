

class InfoBox(pygame.sprite.Sprite):
    def __init__(self, x, y, size, text, color="white"):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, self.size, self.size), 2)
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.position.x + 5, self.position.y + 5))