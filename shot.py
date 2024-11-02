import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2):
        super().__init__(position, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,  SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)