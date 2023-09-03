import pygame
from pygame.sprite import Group

class DefaultHealthBar(pygame.sprite.Sprite):
    def __init__(self, *groups: Group, height, length, owner) -> None:
        self.owner = owner
        self.offset = pygame.Vector2(0, -owner.rect.height/2 - 6)
        self.rect = pygame.Rect(0, 0, length, height)
        self.rect.center = owner.rect.center + self.offset

        self.default_image = pygame.Surface((length, 1.2*height))
        self.default_image.fill('black')
        self.background_rect = pygame.Rect(0, height/10, length, height)
        pygame.draw.rect(self.default_image, (255,255,255,0), self.background_rect, 0, int(height/2))

        self.image = self.default_image.copy()
        
        super().__init__(*groups)

    def update(self, dt):
        if not self.owner.alive():
            self.kill()

        self.rect.center = self.owner.rect.center + self.offset
        
        percent = int(self.owner.hp/self.owner.full_hp * 100)
        color = 'red'
        if percent > 70:
            color = 'green'
        elif percent > 30 and percent <= 70:
            color = 'yellow'

        self.image.fill('black')
        pygame.draw.rect(self.image, 'gray', self.background_rect, 0, int(self.rect.height/2))
        rect = pygame.Rect(0, self.rect.height/10, self.rect.width * percent/100, self.rect.height)
        pygame.draw.rect(self.image, color, rect, 0, int(self.rect.height/2))
