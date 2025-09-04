import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, name):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.name = name


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # print(f"Rotating {self.rotation}")

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # print(f"Moving {self.position}")


    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        # WASD => ZQSD and added arrows
        if keys[pygame.K_q] | keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_z] | keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] | keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_e] | keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shot_timer = PLAYER_SHOT_COOLDOWN



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]