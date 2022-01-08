import pyglet
import math
import random

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world!',
                          font_size=36,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')

ani = pyglet.resource.animation('cat3.gif')
ani2 = pyglet.resource.animation('mouse.gif')

sprites = [pyglet.sprite.Sprite(img=ani) for i in range(3)]
sprites = sprites + [pyglet.sprite.Sprite(img=ani2) for i in range(5)]
for sprite in sprites:
    sprite.x = random.randint(0, window.width)
    sprite.y = random.randint(0, window.height)
    sprite.frame_index = random.randint(0, int(ani.get_duration()))
    sprite.dx = random.randint(-20,20)
    sprite.dy = random.randint(-10,10)
    if sprite.dx > 0:
        sprite.scale_x = -1
    
@window.event
def on_draw():
    window.clear()
    #label.draw()
    for sprite in sprites:
        sprite.x = (sprite.x + sprite.dx) % window.width
        sprite.y = (sprite.y + sprite.dy) % window.height
        sprite.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
        ('v2i', (10, 15, 30, 35))
    )
    cx = 100
    cy = 100
    t = ()
    r = 10
    for i in range(10):
        a = (i % 10) / 5 * math.pi
        x = r * math.sin(a)
        y = r * math.cos(a)
        t = t + (cx + x, cy + y)
    #print(t)
    pyglet.graphics.draw(10, pyglet.gl.GL_LINE_LOOP,
        ('v2f', t)
    )
print("abc")

#window2 = pyglet.window.Window()

def run():
    pyglet.app.run()