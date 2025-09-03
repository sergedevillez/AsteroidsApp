import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()

        # limit the framerate to 60FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
