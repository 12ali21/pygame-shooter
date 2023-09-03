import pygame
from healthbar import PlayerHealthBar

screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

group = pygame.sprite.Group()

bar = PlayerHealthBar(group, height=10, length=200, full_hp=1000, position=(300,300))

running = True

hp = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hp +=1
    bar.update(hp)

    screen.fill('pink')
    
    # Draw here
    group.draw(screen)
    # screen.blit(bar.surface, bar.rect)

    pygame.display.flip()
    dt = clock.tick(60)

    