import pygame
from pygame.sprite import Group
import util
import math

class Gun(pygame.sprite.Sprite):
    def __init__(self, *groups: Group, wielder, dist_to_center) -> None:
        super().__init__(*groups)
        self.wielder = wielder
        print(dist_to_center)
        self.original_image, self.original_rect = util.load_image("minigun.png", scale=0.5)

        self.image = self.original_image
        self.rect = self.original_rect

    def update(self, dt):
        self.image = pygame.transform.rotate(self.original_image, (self.facing-70))
        self.rect = self.image.get_rect()
        
        offset_vector = pygame.Vector2(0, -40)
        pivot_vector = pygame.Vector2(self.wielder.rect.width/2, 0)
        sum_vector = offset_vector + pivot_vector
        offset_angle = sum_vector.angle_to((0,1))
        print(self.facing, offset_angle)
        sum_vector = sum_vector.rotate(-self.facing + 90)
        print(sum_vector)
        self.rect.center = self.wielder.rect.center + sum_vector


    def face_direction(self, direction):
        self.facing = direction