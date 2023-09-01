import pygame
from pygame.sprite import Group
import util
from weapon import MiniGun

class Player(pygame.sprite.Sprite):
    weapon = None
    player_speed = 200

    def __init__(self, *groups: Group, coordinates: tuple) -> None:
        super().__init__(*groups)
        self.image, self.rect = util.load_image("player.png", scale=0.65)
        self.rect.center = coordinates

    def update(self, dt):
        

        # Get pressed keys
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.rect.y -= dt * self.player_speed
        if(keys[pygame.K_s]):
            self.rect.y += dt * self.player_speed
        if(keys[pygame.K_d]):
            self.rect.x += dt * self.player_speed
        if(keys[pygame.K_a]):
            self.rect.x -= dt * self.player_speed

        if(self.weapon):
            if(pygame.mouse.get_pressed(3)[0] == True):
                self.weapon.shooting = True
            else:
                self.weapon.shooting = False


    def assign_weapon(self, weapon: MiniGun):
        self.weapon = weapon
