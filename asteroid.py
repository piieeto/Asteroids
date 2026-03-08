import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen, color="white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            position = pygame.Vector2(self.position)
            asteroid1 = Asteroid(position.x, position.y, new_radius)
            asteroid2 = Asteroid(position.x, position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2