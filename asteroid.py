import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,  self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return         
        random_angle = random.uniform(20, 50)
        new_angle1 = self.velocity.rotate(random_angle)
        new_angle2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos1 = pygame.math.Vector2(self.position)
        pos2 = pygame.math.Vector2(self.position)
        asteroid1 = Asteroid(position=self.position, radius=new_radius, velocity=new_angle1 * 1.2)
        asteroid2 = Asteroid(position=self.position, radius=new_radius, velocity=new_angle2 * 1.2)
        for container in self.containers:
            container.add(asteroid1)
            container.add(asteroid2)


        