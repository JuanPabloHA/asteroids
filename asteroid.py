import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        first_direction = self.velocity.rotate(angle)
        second_direction = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        mini_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        mini_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        mini_asteroid_1.velocity = first_direction * 1.2
        mini_asteroid_2.velocity = second_direction * 1.2