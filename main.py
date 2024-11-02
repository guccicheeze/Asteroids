import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys




def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)
    player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0, rect=None, special_flags=0)
        dt = clock.tick(60)/1000
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        updatable.update(dt)
        pygame.display.flip()



if __name__ == "__main__":
    main()
