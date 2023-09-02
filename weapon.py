import pygame
from pygame.sprite import Group
import util
import math
import random
from projectile import MinigunBullet
from groups import *

class MiniGun(pygame.sprite.Sprite):
    

    def __init__(self, *groups: Group, wielder, dist_to_center) -> None:
        self.shooting = False
        self.fire_rate = 4000
        self.time_between_shots = 0
        self.shooting_started = False

        self.shooting_sound = util.load_sound('minigun_shooting.mp3')
        
        super().__init__(*groups)
        self.wielder = wielder
        print(dist_to_center)
        self.original_image, self.original_rect = util.load_image("minigun.png", scale=0.35)

        self.image = self.original_image
        self.rect = self.original_rect

    def update(self, dt):
        
        # need wielder facing for fixing the position of gun
        wielder_facing = (pygame.Vector2(self.target_pos) - self.wielder.rect.center).angle_to((0,0))
        # and gun faces this direction
        gun_facing = (pygame.Vector2(self.target_pos) - self.rect.center).angle_to((0,0))

        # FIXME: minigun goes crazy when target is close enough
        # a limit on how close the gun can shoot
        if (pygame.Vector2(self.target_pos) - self.wielder.rect.center).length() < 50:
            gun_facing = wielder_facing + 50



        # rotating the gun first
        self.image = pygame.transform.rotate(self.original_image, (gun_facing)-90)
        self.rect = self.image.get_rect()
        
        # now fixing the gun position
        # first create offset vectors in the original position (Gun and character facing up)
        offset_vector = pygame.Vector2(-10, -25)
        pivot_vector = pygame.Vector2(self.wielder.original_rect.width/2, 0)
        sum_vector = offset_vector + pivot_vector


        # now rotate the vectors to character direction
        sum_vector = sum_vector.rotate(-wielder_facing + 90)

        # an offset for the weapon wielding point
        weapon_center_offset = pygame.Vector2(0, -self.original_rect.height/2).rotate(-gun_facing+ 90)


        # fixing the gun position from center of the character and offset by the sum vector
        self.rect.center = self.wielder.rect.center + sum_vector + weapon_center_offset

        # shoot bullets if the trigger is on
        if(self.shooting):
            self.shoot(dt, gun_facing)
        else:
            self.time_between_shots = 0


    def set_target(self, target_pos):
        self.target_pos = target_pos

    def set_shooting(self, shooting:bool):
        self.shooting = shooting
        if(shooting and not self.shooting_started):
            self.shooting_started = True
            self.shooting_sound.play(-1)
        elif(not shooting):
            self.shooting_started = False
            self.shooting_sound.stop()
        

    def shoot(self, dt, direction):
        self.time_between_shots += dt
        if(self.time_between_shots >= 60/self.fire_rate):
            self.time_between_shots = 0

            # this vector is needed to shoot from end of the barrel
            offset_vector = pygame.Vector2(0, self.original_rect.height/2)
            offset_vector = offset_vector.rotate(-direction-90)

            # recoil to make it more natural
            recoil = 1.5
            direction_offset = random.randint(-recoil*10, +recoil*10)/10

            MinigunBullet(all_sprites_group, player_projectile_group, starting_pos=self.rect.center + offset_vector, direction=direction+direction_offset)
