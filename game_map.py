import numpy as np
from perlin_noise import PerlinNoise
import pygame

def generate(n_tiles : pygame.Vector2, seed=None, tile_size=10):
    return Map(n_tiles, seed, tile_size)


OCTAVES = 5
BACKGROUND_COLOR = (145, 117, 93)
TILE_COLOR = (82, 44, 11)

class Map:
    surface = None
    def __init__(self, n_tiles: pygame.Vector2, seed=None, tile_size=10) -> None:
        self.n_tiles = n_tiles
        self.tile_size = tile_size

        self.noise = PerlinNoise(octaves=OCTAVES,seed=seed)
        self.map_tiles = np.zeros(n_tiles, dtype=np.bool_)
        
        for x in range(n_tiles[0]):
            for y in range(n_tiles[1]):
                n = self.noise((x/n_tiles[0], y/n_tiles[1]))
                n = (n+1)/2

                if n>0.53:
                    self.map_tiles[x][y] = True

    def get_surface(self):
        if not self.surface:
            surface_size = (self.n_tiles[0] * self.tile_size, self.n_tiles[1] * self.tile_size)
            self.surface = pygame.Surface(surface_size)
            self.surface.fill(BACKGROUND_COLOR)

            size = self.map_tiles.shape
            for x in range(size[0]):
                for y in range(size[1]):
                    if self.map_tiles[x][y]:
                        rect = pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size)
                        pygame.draw.rect(self.surface, TILE_COLOR, rect)
        return self.surface
