import math
import pygame
import random
import util

from pygame.sprite import Group

class Projectile(pygame.sprite.Sprite):
    def __init__(self, *groups: Group, rect: pygame.Rect , image, direction, speed, damage) -> None:
        super().__init__(*groups)

        self.image = image
        self.rect = rect

        self.speed = speed
        self.direction = direction

        self.damage = damage
    
    def update(self, dt):
        angle = math.radians(self.direction)
        self.rect = self.rect.move(math.cos(angle) * self.speed * dt, -math.sin(angle) * self.speed * dt)


        # projectile bounds
        screen = pygame.display.get_surface()
        if(self.rect.x > screen.get_width() or self.rect.x < 0):
            self.kill()
        elif(self.rect.y > screen.get_height() or self.rect.y < 0):
            self.kill()
        
class MinigunBullet(Projectile):
    def __init__(self, *groups: Group, starting_pos, direction) -> None:
        random_scale = random.randint(1,10)/10
        self.image, self.rect = util.load_image('minigun_bullet.png', scale=random_scale)

        self.image = pygame.transform.rotate(self.image, direction-90)
        self.rect = self.image.get_rect()
        self.rect.center = starting_pos

        super().__init__(*groups, rect=self.rect, image=self.image, direction=direction, speed=5000, damage=8)


