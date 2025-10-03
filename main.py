import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Sprites groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initialize spritres into groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    Score.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 'Serge')
    asteroidfield = AsteroidField()
    score = Score(10, 10)

    dt = 0

    current_page = "menu"

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        if current_page == "menu":
            print('menu')
            current_page = "play"

        elif current_page == "play":
            screen.fill("black")
            updatables.update(dt)
            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    print("Game over!")
                    current_page = "game_over"
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.check_collision(shot):
                        shot.kill()
                        score_to_add = asteroid.split()
                        score.add_score(score_to_add)
            for drawable in drawables:
                drawable.draw(screen)

            pygame.display.flip()

            # limit the framerate to 60FPS
            dt = clock.tick(60) / 1000

        elif current_page == "game_over":
            # save score to score file
            # WARNING : if exit is commented, the score saving will loop
            score.save_score(player, 'scores.json')

            # TODO : show score and retry/close choice
            pygame.time.wait(1000)
            exit(0)


if __name__ == "__main__":
    main()
