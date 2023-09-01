import pygame
from pygame.sprite import Group
import util
import math
import random
from projectile import MinigunBullet

class MiniGun(pygame.sprite.Sprite):
    

    def __init__(self, *groups: Group, wielder, dist_to_center) -> None:
        self.shooting = False
        self.fire_rate = 4000
        self.time_between_shots = 0
        
        super().__init__(*groups)
        self.wielder = wielder
        print(dist_to_center)
        self.original_image, self.original_rect = util.load_image("minigun.png", scale=0.5)

        self.image = self.original_image
        self.rect = self.original_rect

    def update(self, dt):
        offset_vector = pygame.Vector2(-20, -40)
        pivot_vector = pygame.Vector2(self.wielder.rect.width/2, 0)

        wielder_facing = (pygame.Vector2(self.target_pos) - self.wielder.rect.center).angle_to((0,0))
        gun_facing = (pygame.Vector2(self.target_pos) - self.rect.center).angle_to((0,0))
        if math.fabs(gun_facing - wielder_facing) > 50:
            gun_facing = wielder_facing + 50
        print(wielder_facing - gun_facing)

        self.image = pygame.transform.rotate(self.original_image, (gun_facing)-90)
        self.rect = self.image.get_rect()
        
        sum_vector = offset_vector + pivot_vector
        sum_vector = sum_vector.rotate(-wielder_facing + 90)
        self.rect.center = self.wielder.rect.center + sum_vector

        if(self.shooting):
            self.shoot(dt, gun_facing)
        else:
            self.time_between_shots = 0


    def set_target(self, target_pos):
        self.target_pos = target_pos

    def set_shooting(self, shooting:bool):
        self.shooting == shooting

    def shoot(self, dt, direction):
        self.time_between_shots += dt

        if(self.time_between_shots >= 60/self.fire_rate):
            self.time_between_shots = 0
            offset_vector = pygame.Vector2(0, self.original_rect.height/2)
            offset_vector = offset_vector.rotate(-direction-90)
            recoil = 1.5
            direction_offset = random.randint(-recoil*10, +recoil*10)/10

            MinigunBullet(util.all_sprites_group, starting_pos=self.rect.center + offset_vector, direction=direction+direction_offset)
