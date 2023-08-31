import pygame
import math
import os
from projectile import Projectile
from player import Player

pygame.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

dt = 0

all_sprites_group = pygame.sprite.Group()
projectiles_group = pygame.sprite.Group()

player = Player(all_sprites_group, coordinates=(100,100))

running = True
while running:
    # Events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button press
            if event.button == 1:
                vector = pygame.Vector2(event.pos) - player.rect.center
                Projectile(all_sprites_group, projectiles_group, rect=player.rect , direction=-math.radians(vector.angle_to((0,0))), speed=1000)
                

    # update
    all_sprites_group.update(dt)    

    # Draw background (DON'T DRAW ANYTHING BEFORE THIS)
    screen.fill((0, 0, 0))
    
    all_sprites_group.draw(screen)
    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.flip()

    # dt(Delta time): time in seconds passed since last frame
    # (needed so dark souls 1 doesn't happen)
    dt = clock.tick(60) / 1000

pygame.quit()