import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        aste1 = Asteroid(self.position.x, self.position.y, new_radius)
        aste1.velocity = self.velocity.rotate(random_angle) * 1.2

        aste2 = Asteroid(self.position.x, self.position.y, new_radius)
        aste2.velocity = self.velocity.rotate(-random_angle)  * 1.2