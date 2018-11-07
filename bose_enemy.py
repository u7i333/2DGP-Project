from pico2d import *
import game_framework
import game_world
from enemy_bullet import Star_Bullet
from enemy_bullet import Bose_Laser_Bullet

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bose_enemy:

    def __init__(self,x = 400 ,y = 300):
        Bose_enemy.image = load_image('bose_enemy.png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.count = 0
        self.time = get_time()
        self.framecount = 0
        self.velocity = 0
        self.bulletcolor = 0
        self.lasertimer = 0

    def shoot_enemy_bullet(self):
        enemy_bullet = Star_Bullet(self.x, self.y, self.bulletdir, self.bulletcolor)
        game_world.add_object(enemy_bullet, 1)

    def shoot_laser_bullet(self):
        enemy_laser_bullet = Bose_Laser_Bullet(self.x,self.y)
        game_world.add_object(enemy_laser_bullet, 1)

    def draw(self):
        if self.velocity == 0:
            self.image.clip_draw(int(self.frame) * 100, 100, 100, 100, self.x, self.y) # 300,800
        else:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)  # 300,800



    def update(self):
        self.frame = (self.frame + 0.1) % 4

        if (self.count == 0):
            self.velocity = 1
            self.y = self.y - self.velocity
            if (self.y < 750):
                self.count = 1


        if(get_time() - self.time > 0.5 and self.count < 4):
            Bose_enemy.shoot_enemy_bullet(self)
            self.bulletcolor = (self.bulletcolor+1)%7
            self.time = get_time()

        if(self.count == 0):
            self.velocity = 1
            self.y = self.y - self.velocity
            if(self.y < 750):
                self.count = 1

        if(self.count == 1):
            self.x -= self.velocity
            self.y -= self.velocity*0.3
            if (self.x < 50):
                 self.count = 2

        if (self.count == 2):
            self.velocity = 0
            self.x += 1
            if (self.x > 550):
                self.count = 3

        if(self.count == 3):
            self.velocity = 1
            self.x -= self.velocity
            self.y += self.velocity*0.3
            if(self.x <= 300):
                self.count = 4
                self.velocity = 0

        if(self.count == 4):
            Bose_enemy.shoot_laser_bullet(self)
            if(self.lasertimer == 0):
                self.lasertimer = get_time()
            if(get_time() - self.lasertimer > 1):
                self.count = 5

        if(self.count == 5):
            self.velocity = 0
            self.x += 1
            if (self.x > 550):
                self.count = 0


        if self.x <= 25:
            game_world.remove_object(self)
