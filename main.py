# Inspiration from Deep Rock Galactic (Rock and Stone!)


import pygame
import math
import os
from projectile import Projectile
from character import *
from weapon import MiniGun
from groups import *
import util

pygame.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]

screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

dt = 0

projectiles_group = pygame.sprite.Group()

player = Player()
gun = MiniGun(wielder=player, dist_to_center=player.rect.width/2)
enemy = Amoebite(all_sprites_group, coordinates=(100,100), target=player)
enemy = Amoebite(all_sprites_group, coordinates=(60,100), target=player)
enemy = Amoebite(all_sprites_group, coordinates=(100,60), target=player)

all_sprites_group.add(gun, player)
player.assign_weapon(gun)


running = True
while running:
    # Events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # Left mouse button press
        #     if event.button == 1:
        #         vector = pygame.Vector2(event.pos) - player.rect.center
        #         p_rect = pygame.rect.Rect(0,0,10,10)
        #         p_rect.center = player.rect.center
        #         Projectile(all_sprites_group, projectiles_group, rect=p_rect , direction=-math.radians(vector.angle_to((0,0))), speed=1000)
    
    gun.set_target(pygame.mouse.get_pos())

    # update
    all_sprites_group.update(dt)    

    # Draw background (DON'T DRAW ANYTHING BEFORE THIS)
    screen.fill('black')
    all_sprites_group.draw(screen)
    pygame.display.flip()

    # dt(Delta time): time in seconds passed since last frame
    # (needed so dark souls 1 doesn't happen)
    dt = clock.tick(60) / 1000

pygame.quit()