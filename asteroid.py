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
        self.position += (self.velocity * dt)

    # TODO: figure why this method is not getting inherited.
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        self.radius -= ASTEROID_MIN_RADIUS

        smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)

        smaller_asteroid_1.velocity = a * 1.2
        smaller_asteroid_2.velocity = b * 1.2
