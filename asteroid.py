import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, white, self.circleshape, 2)

    def move(self, dt):
        