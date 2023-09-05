import pygame
from perlin_noise import PerlinNoise
import math
import game_map


screen_size = (800,600)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
clock = pygame.time.Clock()


running = True

hp = 10
seed = 1234

g_map = game_map.generate((200,200), seed=seed, tile_size=25)
generated_map = g_map.get_surface()
# generated_map = pygame.Surface(screen_size)
# generated_map.fill((145, 117, 93))
# for x in range(screen_size[0]):
#     for y in range(screen_size[1]):
#         n = math.fabs(noise([x*noise_scale, y*noise_scale]))
#         if(n>0.1):
#             generated_map.set_at([x, y], (82, 44, 11))
        

print("Map generated!")

x, y = 0,0
v = 1000
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y += v*dt/1000
    if keys[pygame.K_d]:
        x -= v*dt/1000
    if keys[pygame.K_s]:
        y -= v*dt/1000
    if keys[pygame.K_a]:
        x += v*dt/1000
    

    screen.fill('white')

    # Draw here
    screen.blit(generated_map, (x,y))
    # screen.blit(bar.surface, bar.rect)

    pygame.display.flip()
    dt = clock.tick(60)
    print(1/dt*1000)
pygame.quit()

# import matplotlib.pyplot as plt
# from perlin_noise import PerlinNoise
# import numpy as np

# noise = PerlinNoise(octaves=15, seed=1)
# xpix, ypix = 200, 200
# pic = np.zeros((xpix, ypix))
# for x in range(xpix):
#     for y in range(ypix):
#         n = (noise((x/xpix, y/ypix)) + 1)/2
#         if(n > 0.5):
#             pic[x][y] = -1
        
# print(pic.min(), pic.max())

# plt.imshow(pic, cmap='gray')
# plt.show()