import pygame
import random
import image
from settings import *
from octo import Mosquito

class Bee(Mosquito):
    def __init__(self):
        #size
        random_size_value = random.uniform(BEE_SIZE_RANDOMIZE[0], BEE_SIZE_RANDOMIZE[1])
        size = (int(BEE_SIZES[0] * random_size_value), int(BEE_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(f"Assets/bee/{1}.png", size=size, flip=moving_direction=="right") ] # load the images
        self.current_frame = 0
        self.animation_timer = 0
        

    def kill(self, mosquitos): # remove the mosquito from the list
        mosquitos.remove(self)
        return -BEE_PENALITY


class Spongebob(Mosquito):
    def __init__(self):
        random_size_value = random.uniform(BEE_SIZE_RANDOMIZE[0], BEE_SIZE_RANDOMIZE[1])
        size = (int(BEE_SIZES[0] * 3.5), int(BEE_SIZES[1] * 3.5))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(f"Assets/bee/spongebob-{nb}.png", size=size, flip=moving_direction=="right") for nb in range(0,16) ] # load the images
        self.current_frame = 0
        self.animation_timer = 0
        
