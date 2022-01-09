import pyglethelper
import pyglet
from pyglet.window import key
from pyglethelper import objmanager
import random

from pyglethelper.objmanager import Object, ObjectManager

objManager = ObjectManager()

class Sprite(Object):
    def __init__(self, window: pyglet.window.Window) -> None:
        super().__init__()
        ani = pyglet.resource.animation('cat3.gif')
        self.sprite = pyglet.sprite.Sprite(img=ani)
        self.boundary = (window.width, window.height)
        self.sprite.x = random.randint(0, window.width)
        self.sprite.y = random.randint(0, window.height)
        self.sprite.frame_index = random.randint(0, int(ani.get_duration()))
        self.sprite.dx = random.randint(-20,20)
        self.sprite.dy = random.randint(-10,10)
        if self.sprite.dx > 0:
            self.sprite.scale_x = -1
    def update(self) -> None:
        self.sprite.x = (self.sprite.x + self.sprite.dx) % self.boundary[0]
        self.sprite.y = (self.sprite.y + self.sprite.dy) % self.boundary[1]
        self.sprite.draw()
        pass

s1 = Sprite(pyglethelper.window)
objManager.add(s1)
s2 = Sprite(pyglethelper.window)
objManager.add(s2)

@pyglethelper.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

@pyglethelper.window.event
def on_draw():
    pyglethelper.window.clear()
    objManager.update()

pyglethelper.run()