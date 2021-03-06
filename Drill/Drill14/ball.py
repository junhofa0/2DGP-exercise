import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None
    bg = None

    def __init__(self):
        if Ball.bg == None:
            Ball.bg = main_state.background
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 800 -1), 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

