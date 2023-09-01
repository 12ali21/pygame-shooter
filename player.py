import pygame
from pygame.sprite import Group
import util
from weapon import Gun

class Player(pygame.sprite.Sprite):


    def __init__(self, *groups: Group, coordinates: tuple) -> None:
        super().__init__(*groups)
        self.image, self.rect = util.load_image("player.png", scale=0.75)
        self.rect.center = coordinates

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
            
        if(pygame.mouse.get_pressed(3)[0] == True):
            self.weapon.set_shooting(True)
        else:
            self.weapon.set_shooting(False)


    def assign_weapon(self, weapon: Gun):
        self.weapon = weapon
