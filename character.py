import pygame
from pygame.sprite import Group
import util
from groups import *
from weapon import MiniGun
import math

class Character(pygame.sprite.Sprite):
    def __init__(self, *groups: Group, image, rect, hp) -> None:
        super().__init__(*groups)
        self.original_image = image
        self.original_rect = rect
        self.image = self.original_image
        self.rect = self.original_rect

        self.hitpoints = hp
    
    def damage(self, amount):
        self.hitpoints -= amount
        if(self.hitpoints <= 0):
            self.kill()



class Player(Character):
    weapon = None
    movement_speed = 200

    def __init__(self, *groups: Group) -> None:
        image, rect = util.load_image("player.png", scale=0.55)
        window_size = pygame.display.get_window_size()
        rect.center = (window_size[0] / 2, window_size[1] / 2)
        super().__init__(*groups, image=image, rect=rect, hp=1000)



    def update(self, dt):
        
        # Get pressed keys
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.rect.y -= dt * self.movement_speed
        if(keys[pygame.K_s]):
            self.rect.y += dt * self.movement_speed
        if(keys[pygame.K_d]):
            self.rect.x += dt * self.movement_speed
        if(keys[pygame.K_a]):
            self.rect.x -= dt * self.movement_speed

        if(self.weapon):
            if(pygame.mouse.get_pressed(3)[0] == True):
                self.weapon.set_shooting(True)
            else:
                self.weapon.set_shooting(False)

        target_pos = pygame.mouse.get_pos()
        direction = (pygame.Vector2(target_pos) - self.rect.center).angle_to((0,0))
        self.image = pygame.transform.rotate(self.original_image, direction-90)
        self.rect = self.image.get_rect(center = self.rect.center)


    def assign_weapon(self, weapon: MiniGun):
        self.weapon = weapon



class Amoebite(Character):
    movement_speed = 250
    def __init__(self, *groups: Group, coordinates, target) -> None:

        image, rect = util.load_image('enemy1.png', scale=0.1)
        rect.center = coordinates

        self.target = target
        super().__init__(*groups, image=image, rect=rect, hp=250)
        
    def update(self, dt):
        target_vector = util.get_vector(self.rect.center, self.target.rect.center)
        direction = target_vector.angle_to((0,0))
        self.image = pygame.transform.rotate(self.original_image, direction - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

        if(target_vector.length() > 100):
            angle_radians = math.radians(direction)
            print(self.rect, end='  ')
            self.rect = self.rect.move(math.cos(angle_radians)*dt*self.movement_speed, -math.sin(angle_radians)*dt*self.movement_speed)
            print(self.rect)
        
        collided_bullets = self.rect.collideobjectsall(player_projectile_group.sprites())
        for b in collided_bullets:
            self.damage(b.damage)
            b.kill()