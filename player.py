import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from pygame.math import Vector2



class Player(CircleShape):
    def __init__(self, position):
        super().__init__(Vector2(position), PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        if self.timer < 0:
            self.timer = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        movement = rotated_vector * PLAYER_SPEED * dt
        self.position += movement

    def shoot(self):
        if self.timer > 0:
            return None
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot_position = pygame.Vector2(self.position)
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot = Shot(shot_position, shot_velocity)
        return new_shot