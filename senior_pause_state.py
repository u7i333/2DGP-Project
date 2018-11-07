import game_framework
from pico2d import *
import main_state

name = "SeniorPauseState"
image = None
blink_time = False


def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def handle_events():
    global blink_time
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            blink_time = False
            game_framework.pop_state()



def draw():
    global blink_time
    global image

    clear_canvas()
    main_state.draw()
    if (blink_time == True):
        image.draw(300, 400)
    update_canvas()
    delay(0.5)

def update():
    global blink_time
    if (blink_time == False):
        blink_time = True
    else:
        blink_time = False

def pause():
    pass


def resume():
    pass

