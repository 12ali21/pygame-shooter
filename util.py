import pygame
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")



# functions to create our resources
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

# returns joined path of default data directory and provided directory
def get_data_dir(dir):
    return os.path.join(data_dir, dir)

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pygame.mixer.Sound(fullname)

    return sound

def get_vector(point1, point2):
    return pygame.Vector2(point2) - pygame.Vector2(point1)

class CallbackTimer():
    started = False
    dt_container = 0

    def __init__(self, cooldown, callback, call_first=False) -> None:
        self.cooldown = cooldown
        self.callback = callback
        self.call_first = call_first

    def update(self, dt):
        if not self.started:
            self.started = True
            if self.call_first:
                self.callback()
        
        self.dt_container += dt
        if(self.dt_container >= self.cooldown):
            self.dt_container = 0
            self.callback()

    def reset(self):
        self.started = False
        self.dt_container = 0
