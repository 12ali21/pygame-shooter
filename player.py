import pygame
from pygame.sprite import Group

class Player(pygame.sprite.Sprite):


    def __init__(self, *groups: Group, coordinates: tuple) -> None:
        super().__init__(*groups)
        self.rect = pygame.Rect(coordinates[0], coordinates[1], 40, 40)
        self.image = pygame.Surface((80, 80))
        pygame.draw.circle(self.image, "red", (40,40), 40)

    def update(self, dt):
        player_speed = 300

        # Get pressed keys
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.rect.y -= dt * player_speed
        if(keys[pygame.K_s]):
            self.rect.y += dt * player_speed
        if(keys[pygame.K_d]):
            self.rect.x += dt * player_speed
        if(keys[pygame.K_a]):
            self.rect.x -= dt * player_speed
