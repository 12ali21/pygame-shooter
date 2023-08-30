import pygame
class Projectile:
    def __init__(self, speed, starting_point:pygame.Vector2 , direction, radius) -> None:
        self.vector = starting_point
        self.speed = speed
        self.direction = direction
        self.radius = radius
