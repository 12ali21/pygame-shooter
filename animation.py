import pygame
import os
import util

class Animator:
    dt_container = 0.
    current_index = 0
    active = ''

    def __init__(self, idle_image):
        self.animations = {}
        self.idle_image = idle_image
        self.current_frame = self.idle_image
    
    # Adds an animation to the dictionary
    def add_animation(self, name, data_dir, scale=1):
        frames_dir = os.listdir(data_dir)
        frames_dir.sort()
        frames = []
        for f in frames_dir:
            image, _ = util.load_image(os.path.join(data_dir, f), scale=scale)
            frames.append(image)
        self.animations[name] = frames

    # Sets the active animation
    def animate(self, name, animation_speed = 5.):
        self.active = name
        self.animation_speed = animation_speed
        self.current_frame = self.animations[self.active][0]

    # Pauses animation
    def stop_animaton(self):
        self.active = ''
        self.dt_container = 0


    def update(self, dt:float):
        if self.active == '':
            return self.current_frame
        # Acts as a timer between frames
        self.dt_container += dt
        if(self.dt_container>=1/self.animation_speed):
            self.dt_container = 0
            # Sets current frame and loop back to start of the animation if needed
            frames = self.animations[self.active]
            if len(frames) > self.current_index:
                self.current_frame = frames[self.current_index]
                self.current_index += 1
            else:
                self.current_frame = frames[0]
                self.current_index = 1
        return self.current_frame