import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        break_radius = self.radius - ASTEROID_MIN_RADIUS

        one = self.velocity.rotate(angle) 
        asteroid = Asteroid(self.position.x, self.position.y, break_radius)
        asteroid.velocity = one * 1.2

        two = self.velocity.rotate(-angle)   
        asteroid = Asteroid(self.position.x, self.position.y, break_radius)
        asteroid.velocity = two *1.2
