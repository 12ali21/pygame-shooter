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


all_sprites_group.add(gun, player)
player.assign_weapon(gun)


running = True
while running:
    # Events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    gun.set_target(pygame.mouse.get_pos())

    # update
    all_sprites_group.update(dt)    

    # Draw background (DON'T DRAW ANYTHING BEFORE THIS)
    screen.fill('pink')
    all_sprites_group.draw(screen)
    pygame.display.flip()

    # dt(Delta time): time in seconds passed since last frame
    # (needed so dark souls 1 doesn't happen)
    dt = clock.tick(60) / 1000

pygame.quit()