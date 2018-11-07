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

name = "MainState"


map = None
heroine = None
blue_enemy = None

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



def enter():
    global map, heroine
    map = Map()
    heroine = Heroine()
    game_world.add_object(heroine, 1)
    #global summontime
    #summontime = get_time()



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
    blue_enemy1 = [Blue_enemy(i,j) for (i,j) in [(600,500),(650,500),(700,500)] ]
    red_enemy = [Red_enemy(i,j) for (i,j) in [(0,500),(-50,500),(-100,500)] ]
    blue_enemy2 = Blue_enemy(600,400)
    black_enemy = Black_enemy(0,450)
    green_enemy = Green_enemy(600,450)


    #if(get_time() - summontime) == 1):
    if (map.y == 1):
        for i in range(0,3):
            game_world.add_object(blue_enemy1[i], 1)

    if (map.y == 50):
        for i in range(0, 3):
            game_world.add_object(red_enemy[i], 1)

    if(map. y == 100):
        game_world.add_object(black_enemy,1)
        game_world.add_object(green_enemy,1)

    if (map.y == 200):
        for i in range(0,3):
            game_world.add_object(blue_enemy1[i], 1)

    if(map.y == 270):
        red_enemy = [Red_enemy(i, j) for (i, j) in [(0, 650), (-50, 650), (-100, 650)]]
        black_enemy = Black_enemy(0,600)
        green_enemy = Green_enemy(600,600)
        game_world.add_object(black_enemy,1)
        game_world.add_object(green_enemy,1)

    if (map.y == 300):
        for i in range(0, 3):
            game_world.add_object(red_enemy[i], 1)
    """
    if (map.y == 500):
        game_world.add_object(blue_enemy2, 1)
    """

    if (map.y == 500):
        bose_enemy = Bose_enemy(300,800)
        game_world.add_object(bose_enemy, 1)

def draw():
    clear_canvas()
    map.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





