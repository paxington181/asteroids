import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    
    print("Starting asteroids!")
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont("Comic Sans MS", 60)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    strscore = "0"
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        screen.fill((0, 0, 0))
        text_surface = my_font.render(strscore, False, (255, 255, 255))
        screen.blit(text_surface, ( 0, 0))

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                print(f"Final score: {score}")
                sys.exit()

        for bullet in shots:
            for asteroid in asteroids:    
                if bullet.collision(asteroid):
                    bullet.kill()
                    score += asteroid.score
                    asteroid.split()

        strscore = str(score)





        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()