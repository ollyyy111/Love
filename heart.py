import pygame
import random
import math


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Particle Animation")
clock = pygame.time.Clock()

BACKGROUND = (8, 3, 15)
PINK = (255, 105, 180)

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

class Particle:
    def __init__(self, target_x, target_y, delay):
        self.start_x = CENTER_X
        self.start_y = CENTER_Y

        self.target_x = target_x + (random.random() - 0.5) * 30
        self.target_y = target_y + (random.random() - 0.5) * 30
        
        
        self.duration = random.uniform(2.0, 4.5)  
        self.delay = delay                     
        self.elapsed_time = 0.0
        
        
        self.x = self.start_x
        self.y = self.start_y

    def update(self, dt):
        
        if self.delay > 0:
            self.delay -= dt
            return

        if self.elapsed_time < self.duration:
            self.elapsed_time += dt
            
            t = min(self.elapsed_time / self.duration, 1.0)
            
            ease = 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2
            
            
            self.x = self.start_x + (self.target_x - self.start_x) * ease
            self.y = self.start_y + (self.target_y - self.start_y) * ease

    def draw(self, surface):
        if self.delay <= 0:

            x = int(self.x)
            y = int(self.y)

            glow = pygame.Surface((30, 30), pygame.SRCALPHA)

            pygame.draw.circle(
                glow,
                (255, 105, 180, 25),
                (15, 15),
                12
            )

            pygame.draw.circle(
                glow,
                (255, 105, 180, 50),
                (15, 15),
                7
            )

            pygame.draw.circle(
                glow,
                (255, 180, 220, 255),
                (15, 15),
                2
            )

            surface.blit(
                glow,
                (x - 15, y - 15),
                special_flags=pygame.BLEND_ALPHA_SDL2
            )

particles = []
num_points = 3000

for i in range(num_points):
    t = (i / num_points) * 2 * math.pi

    hx = 16 * math.sin(t) ** 3
    hy = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    
    final_target_x = CENTER_X + hx * 12

    final_target_y = CENTER_Y - hy * 12  
    
   
    delay = i * 0.004
    
    particles.append(Particle(final_target_x, final_target_y, delay))

running = True
while running:
    dt = clock.tick(60) / 1000.0 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.update(dt)

    screen.fill(BACKGROUND)
    for particle in particles:
        particle.draw(screen)
        
    pygame.display.flip()

pygame.quit()