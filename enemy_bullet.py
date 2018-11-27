from pico2d import *
import game_world
import game_framework
import main_state
import heroine


class Blue_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Blue_Enemy_Bullet.image == None:
            Blue_Enemy_Bullet.image = load_image('blue_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 5, self.y - 5,  self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity*0.5
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            game_world.remove_object(main_state.heroine)


class Black_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Black_Enemy_Bullet.image == None:
            Black_Enemy_Bullet.image = load_image('black_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity*0.5
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            game_world.remove_object(main_state.heroine)



class Red_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Red_Enemy_Bullet.image == None:
            Red_Enemy_Bullet.image = load_image('red_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.hx, self.hy = main_state.heroine.x, main_state.heroine.y
        self.countx = (self.hx - self.x)/900
        self.county = (self.hy - self.y)/900

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5


    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.x += self.countx
        self.y += self.county

        if self.y < 25 or self.y > 800 - 25 or self.x < 25 or self.y> 800-25 :
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            game_world.remove_object(main_state.heroine)



class Green_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Green_Enemy_Bullet.image == None:
            Green_Enemy_Bullet.image = load_image('green_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.hx, self.hy = main_state.heroine.x, main_state.heroine.y
        self.countx = (self.hx - self.x) / 900
        self.county = (self.hy - self.y) / 900

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.countx
        self.y += self.county

        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            game_world.remove_object(main_state.heroine)

class Special_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocityx= 1, velocityy= 1  ):
        if Special_Enemy_Bullet.image == None:
            Special_Enemy_Bullet.image = load_image('special_enemy_bullet.png')
        self.x, self.y, self.velocityx, self.velocityy = x, y, velocityx, velocityy

    def draw(self):
        self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - 15, self.y - 15,  self.x + 15, self.y + 15

    def update(self):
        self.x -= self.velocityx
        self.y -= self.velocityy

        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            game_world.remove_object(main_state.heroine)



class Star_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1, frame = 0):
        if Star_Bullet.image == None:
            Star_Bullet.image = load_image('star_bullet.png')
        self.x, self.y, self.velocity, self.frame = x, y, velocity, frame

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 15,  self.x + 15, self.y + 15

    def update(self):
        self.y -= self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            game_world.remove_object(main_state.heroine)


class Bose_Laser_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Bose_Laser_Bullet.image == None:
            Bose_Laser_Bullet.image = load_image('master_spark.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.bullettime = get_time()
        self.time = 0
        self.count = 0

    def get_bb(self):
        return self.x - 150, self.y - 775,  self.x + 150, self.y - 175

    def draw(self):
        #self.image.clip_draw(125 - self.drawframeX, 0, 50+self.sizeframeX, 50+self.sizeframeY, self.x, self.y-400)
        self.image.clip_draw(300 * self.frame, 0, 300, 750, self.x, self.y-400)

    def update(self):
        if get_time() - self.bullettime > 0.05:
            self.frame = (self.frame + 1) % 11
            self.bullettime = get_time()
        if self.frame > 5:
            if main_state.collide(main_state.heroine, self):
                game_world.remove_object(main_state.heroine)
        if self.frame > 9 :
            game_world.remove_object(self)
