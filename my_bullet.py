from pico2d import *
import game_world
import game_framework

import main_state

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class My_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if My_Bullet.image == None:
            My_Bullet.image = load_image('bullet.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 20,  self.x + 10, self.y + 20

    def update(self):
        #self.y += self.velocity
        self.y += RUN_SPEED_PPS*0.2

        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)

        if main_state.collide(main_state.blue_enemy, self):
            main_state.blue_enemy.hp -= 1
            #game_world.remove_object(main_state.blue_enemy)

        for i in range(0, 3):
            if main_state.collide(main_state.blue_enemys1[i], self):
                main_state.blue_enemys1[i].hp -= 1
                #game_world.remove_object(main_state.blue_enemys1[i])

        if main_state.collide(main_state.bose_enemy, self):
            main_state.bose_enemy.hp -= 1
            #game_world.remove_object(main_state.bose_enemy)

        for i in range(0, 3):
            if main_state.collide(main_state.black_enemys1[i], self):
                main_state.black_enemys1[i].hp -= 1
                #game_world.remove_object(main_state.black_enemys1[i])

        if main_state.collide(main_state.red_enemy, self):
            main_state.red_enemy.hp -= 1

        if main_state.collide(main_state.green_enemy, self):
            main_state.green_enemy.hp -= 1

        if main_state.collide(main_state.special_enemy, self):
            main_state.special_enemy.hp -= 1

class Speciel_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Speciel_Bullet.image == None:
            Speciel_Bullet.image = load_image('special_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)