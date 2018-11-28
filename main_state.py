import random
import json
import os

from pico2d import *
import game_world
import game_framework
import title_state
#import pause_state
import senior_pause_state
from heroine import Heroine
from norml_enemy import Blue_enemy
from norml_enemy import Black_enemy
from norml_enemy import Red_enemy
from norml_enemy import Green_enemy
from bose_enemy import Bose_enemy
from norml_enemy import Special_enemy

from enemy_bullet import Blue_Enemy_Bullet

name = "MainState"


PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


map = None
heroine = None
blue_enemy = None
blue_enemys1 = None
bose_enemy = None
red_enemy = None
green_enemy = None
special_enemy = None

class Map:
    y = 0
    frame = 0.25

    def __init__(self):
        self.image = load_image('shooting_ground.bmp')


    def draw(self):
        self.image.draw(400, +4850 - 600 - self.y)

    def update(self):
        self.y += self.frame

        if(self.y > 8000):
            self.y = 0

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global map, heroine, blue_enemy, blue_enemys1,black_enemys1, bose_enemy, red_enemy, green_enemy, special_enemy
    map = Map()
    heroine = Heroine()
    blue_enemy = Blue_enemy(600, 400)
    game_world.add_object(heroine, 1)
    #global summontime
    #summontime = get_time()
    blue_enemys1 = [Blue_enemy(i, j) for (i, j) in [(600, 700), (650, 700), (700, 700)]]
    black_enemys1 = [Black_enemy(i, j) for (i, j) in [(0, 700), (-50, 700), (-100, 700)]]
    bose_enemy = Bose_enemy(300, 800)
    red_enemy = Red_enemy(0,700)
    green_enemy = Green_enemy(600, 700)
    special_enemy = Special_enemy(300,810)

def exit():
    global map
    game_world.clear()
    del(map)

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(senior_pause_state)
        else:
            heroine.handle_event(event)

def update():
    map.update()

    for game_object in game_world.all_objects():
        game_object.update()

    if(map.y == 1000):
        game_world.add_object(bose_enemy, 1)

    if (map.y == 1):
        game_world.add_object(blue_enemy, 1)

    if(map.y == 50):
        for i in range(0, 3):
            game_world.add_object(blue_enemys1[i], 1)

    if(map.y == 200):
        for i in range(0, 3):
            game_world.add_object(black_enemys1[i], 1)

    if(map.y == 350):
        game_world.add_object(red_enemy, 1)


    if(map.y == 400):
        game_world.add_object(green_enemy, 1)

    if(map.y == 500):
        game_world.add_object(special_enemy,1)





def draw():
    clear_canvas()
    map.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





