import pygame
from pygame.sprite import Group
import util
from groups import *
from weapon import MiniGun
import math
from healthbar import DefaultHealthBar
from animation import Animator

class Character(pygame.sprite.Sprite):
    def __init__(self, *groups: Group, image, rect: pygame.Rect, hp) -> None:
        super().__init__(*groups)
        self.original_image = image
        self.original_rect = rect
        self.image = self.original_image
        self.rect = self.original_rect
        self.full_hp = hp
        self.hp = hp

        self.animator = Animator(self.original_image)
    
    def damage(self, amount):
        self.hp -= amount
        if(self.hp <= 0):
            self.kill()



class Player(Character):
    weapon = None
    movement_speed = 200

    def __init__(self, *groups: Group) -> None:
        image, rect = util.load_image("player.png", scale=0.60)
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
    WALK_ANIMATION = 'walk'

    is_walking = False

    full_hp = 250
    bite_damage = 20
    bite_range = 100
    bite_range_offset = 20


    def __init__(self, *groups: Group, coordinates, target:Character) -> None:
        image, rect = util.load_image('amoebite/amoebite.png', scale=0.1)
        rect.center = coordinates
        self.target = target
        super().__init__(*groups, image=image, rect=rect, hp=self.full_hp)
        

        self.animator.add_animation(self.WALK_ANIMATION, util.get_data_dir('amoebite/walk'), scale=0.1)
        self.bite_timer = util.CallbackTimer(1, self.bite_target, call_first=True)
        
        self.healthbar = DefaultHealthBar(all_sprites_group, height=5, length=40, owner=self)
    
        
    def update(self, dt):
        self.default_image = self.animator.update(dt)
        # Rotating towards target
        target_vector = util.get_vector(self.rect.center, self.target.rect.center)
        direction = target_vector.angle_to((0,0))
        self.image = pygame.transform.rotate(self.default_image, direction - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Moving towards target
        if(target_vector.length() > self.bite_range - self.bite_range_offset):
            if(not self.is_walking):
                self.is_walking = True
                self.animator.animate(self.WALK_ANIMATION, animation_speed=10)

            angle_radians = math.radians(direction)
            self.rect = self.rect.move(math.cos(angle_radians)*dt*self.movement_speed, -math.sin(angle_radians)*dt*self.movement_speed)

        else:
            self.is_walking = False
            self.animator.stop_animaton()
            self.bite_timer.update(dt)
        
        collided_bullets = self.rect.collideobjectsall(player_projectile_group.sprites())
        for b in collided_bullets:
            self.damage(b.damage)
            b.kill()

    def bite_target(self):
        if util.get_vector(self.rect.center, self.target.rect.center).length() <= self.bite_range:
            self.target.damage(self.bite_damage)
            print("Bite {} hp: {}".format(self.target, self.target.hp))
        else:
            self.bite_timer.reset()
