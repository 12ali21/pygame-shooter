import math
import pygame

from pygame.sprite import Group

class Projectile(pygame.sprite.Sprite):
    def __init__(self, *groups: Group, rect: pygame.Rect , direction, speed) -> None:
        super().__init__(*groups)

        self.rect = rect
        self.image = pygame.Surface(rect.size)
        pygame.draw.circle(self.image, "gray", (self.rect.width/2, self.rect.height/2), self.rect.width/2)

        self.speed = speed
        self.direction = direction
    
    def update(self, dt):
        self.rect = self.rect.move(math.cos(self.direction) * self.speed * dt, math.sin(self.direction) * self.speed * dt)
        print(self.rect)
        # projectile bounds
        screen = pygame.display.get_surface()
        if(self.rect.x > screen.get_width() or self.rect.x < 0):
            self.remove()
        elif(self.rect.y > screen.get_height() or self.rect.y < 0):
            self.remove()
        
