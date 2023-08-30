import pygame
import math
from projectile import Projectile

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

dt = 0

# Player variables
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
player_speed = 200

# Projectiles Variables
projectiles = []

def draw_projectiles(screen, projectiles:list[Projectile], dt):
    for p in projectiles:
        print(p.vector)
        p.vector = pygame.Vector2(p.vector.x + math.cos(p.direction) * p.speed * dt, p.vector.y + math.sin(p.direction) * p.speed * dt)

        # projectile bounds
        if(p.vector.x > screen.get_width() or p.vector.x < 0):
            projectiles.remove(p)
        elif(p.vector.y > screen.get_height() or p.vector.y < 0):
            projectiles.remove(p)
        else:
            pygame.draw.circle(screen, "gray", p.vector, p.radius)



running = True
while running:
    # Events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button press
            if event.button == 1:
                vector = pygame.Vector2(event.pos) - player_pos
                projectiles.append(Projectile(1000, player_pos, -math.radians(vector.angle_to((0,0))), 10))
                
                

    # Detect keys
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_w]):
        player_pos.y -= dt * player_speed
    if(keys[pygame.K_s]):
        player_pos.y += dt * player_speed
    if(keys[pygame.K_d]):
        player_pos.x += dt * player_speed
    if(keys[pygame.K_a]):
        player_pos.x -= dt * player_speed
        

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, "red", player_pos, 40)
    draw_projectiles(screen, projectiles, dt)

    pygame.display.flip()

    # dt(Delta time): time in seconds passed since last frame
    dt = clock.tick(60) / 1000

pygame.quit()