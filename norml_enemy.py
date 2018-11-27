from pico2d import *
import game_framework
import game_world
from enemy_bullet import Blue_Enemy_Bullet
from enemy_bullet import Black_Enemy_Bullet
from enemy_bullet import Red_Enemy_Bullet
from enemy_bullet import Green_Enemy_Bullet
from enemy_bullet import Special_Enemy_Bullet
import main_state

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Blue_enemy:

    def __init__(self,x = 400 ,y = 300):
        Blue_enemy.image = load_image('blue_enemy(L).png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.time = get_time()

    def shoot_enemy_bullet(self):
        enemy_bullet = Blue_Enemy_Bullet(self.x, self.y,self.bulletdir * RUN_SPEED_PPS * 0.01)
        game_world.add_object(enemy_bullet, 1)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if(get_time() - self.time > 1):
            Blue_enemy.shoot_enemy_bullet(self)
            self.time = get_time()

        self.x = self.x - 0.2

        if self.x <= 25:
            game_world.remove_object(self)


class Green_enemy:

    def __init__(self,x = 400 ,y = 300):
        Green_enemy.image = load_image('green_enemy(L).png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.time = get_time()

    def shoot_enemy_bullet(self):
        enemy_bullet = Green_Enemy_Bullet(self.x, self.y,self.bulletdir * RUN_SPEED_PPS * 0.01)
        game_world.add_object(enemy_bullet, 1)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if(get_time() - self.time > 0.5):
            Green_enemy.shoot_enemy_bullet(self)
            self.time = get_time()

        self.x = self.x - 0.2

        if self.x <= 25:
            game_world.remove_object(self)


class Black_enemy:

    def __init__(self,x = 400 ,y = 300):
        Black_enemy.image = load_image('black_enemy(R).png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.time = get_time()

    def shoot_enemy_bullet(self):
        enemy_bullet = Black_Enemy_Bullet(self.x, self.y,self.bulletdir * RUN_SPEED_PPS * 0.01)
        game_world.add_object(enemy_bullet, 1)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if(get_time() - self.time > 1):
            Black_enemy.shoot_enemy_bullet(self)
            self.time = get_time()

        self.x = self.x + 0.2

        if self.x >= 600:
            game_world.remove_object(self)


class Red_enemy:

    def __init__(self,x = 400 ,y = 300):
        Red_enemy.image = load_image('red_enemy(R).png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.time = get_time()

    def shoot_enemy_bullet(self):
        enemy_bullet = Red_Enemy_Bullet(self.x, self.y,self.bulletdir * RUN_SPEED_PPS * 0.01)
        game_world.add_object(enemy_bullet, 1)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if(get_time() - self.time > 0.5):
            Red_enemy.shoot_enemy_bullet(self)
            self.time = get_time()

        self.x = self.x + 0.2

        if self.x >= 600:
            game_world.remove_object(self)

class Special_enemy:

    def __init__(self,x = 400 ,y = 300):
        Special_enemy.image = load_image('special_enemy.png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.time = get_time()

    def shoot_enemy_bullet(self):
        enemy_bullet1 = Special_Enemy_Bullet(self.x, self.y, 1,1)
        enemy_bullet2 = Special_Enemy_Bullet(self.x, self.y, 0.5, 1)
        enemy_bullet3 = Special_Enemy_Bullet(self.x, self.y, 0, 1)
        enemy_bullet4 = Special_Enemy_Bullet(self.x, self.y, -0.5, 1)
        enemy_bullet5 = Special_Enemy_Bullet(self.x, self.y, -1, 1)
        game_world.add_object(enemy_bullet1, 1)
        game_world.add_object(enemy_bullet2, 1)
        game_world.add_object(enemy_bullet3, 1)
        game_world.add_object(enemy_bullet4, 1)
        game_world.add_object(enemy_bullet5, 1)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 75, 0, 75, 75, self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if(get_time() - self.time > 0.7):
            Special_enemy.shoot_enemy_bullet(self)
            self.time = get_time()

        self.y = self.y - 0.1

        if self.x >= 600:
            game_world.remove_object(self)