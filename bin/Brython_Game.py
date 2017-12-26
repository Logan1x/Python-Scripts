if __name__ == '__main__':
    import sys, os, webbrowser
    url = "file:///" + os.getcwd() + "/index.html"
    if webbrowser.open_new(url):
        webbrowser.open_new(url)
    else:
        print("You need to execute file index.html")
        os.system("Pause")
    sys.exit()

from browser import document as doc
from browser import alert, html
from browser.timer import request_animation_frame as raf
import random
import time

class Game:
    canvas = None
    context = None

class SET:
    WINDOW_SIZE = (800, 570)
    FPS = 60

class Rect:
    def __init__(self, pos=(0,0), size=(10,10)):
        (self._x, self._y) = pos
        (self._w, self._h) = size

    def __getattr__(self, name):
        if name == 'top' or name == 'y':
            return self._y
        elif name == 'left' or name == 'x':
            return self._x
        elif name == 'bottom':
            return self._y + self._h
        elif name == 'right':
            return self._x + self._w
        elif name == 'size':
            return self._w, self._h
        elif name == 'width':
            return self._w
        elif name == 'height':
            return self._h
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'top' or name == 'y':
            self._y = int(value)
        elif name == 'left' or name == 'x':
            self._x = int(value)
        elif name == 'bottom':
            self._y = int(value) - self._h
        elif name == 'right':
            self._x = int(value) - self._w
        elif name == 'size':
            if int(value[0]) > 0 and int(value[1]) > 0:
                self._w, self._h = int(value)
        elif name == 'width':
            if int(value) > 0:
                self._w = int(value)
        elif name == 'height':
            if int(value) > 0:
                self._h = int(value)
        else:
            super().__setattr__(name, value)

    def get_collide(self, other_rect):
        return self._rect_get_collide(other_rect)

    def draw(self):
        Game.context.fillRect(self.x, self.y, self.width, self.height)

    def _rect_get_collide(a, b):
        return a.x + a.width > b.x and b.x + b.width > a.x and \
        a.y + a.height > b.y and b.y + b.height > a.y

class Level:
    def __init__(self):
        self.groupPlatform = list()
        self.get_map()
        self.allPlatform = {
            "Platform": self.groupPlatform,
        }

    def draw(self):
        for e in self.groupPlatform:
            e.draw()

    def get_map(self):
        self.groupPlatform.append(Rect((349,450),(100,10)))
        self.groupPlatform.append(Rect((349,250),(100,10)))
        self.groupPlatform.append(Rect((49,400),(200,10)))
        self.groupPlatform.append(Rect((549,400),(200,10)))
        self.groupPlatform.append(Rect((549,150),(200,10)))
        self.groupPlatform.append(Rect((49,150),(200,10)))
        self.groupPlatform.append(Rect((349,50),(100,10)))

class Puce:
    def __init__(self, level, pos=(10,10), size=(10,10)):
        self.rect = Rect(pos,size)
        self.change_x, self.change_y = 0, 0
        self.level = level
        self.compteur = random.uniform(0, 2)
        self.chrono = time.time()
        self.toggle_walk = True

    def update(self):
        if self.toggle_walk: self.go_left()
        elif not self.toggle_walk: self.go_right()
        self.calc_gravity()
        self.rect.x += self.change_x

        for platform in self.level.allPlatform["Platform"]:
            if self.rect.get_collide(platform):
                if self.change_x > 0:
                    self.rect.right = platform.left
                elif self.change_x < 0:
                    self.rect.left = platform.right
                self.toggle_walk = not self.toggle_walk
                self.change_y = -2

        self.rect.y += self.change_y

        for platform in self.level.allPlatform["Platform"]:
            if self.rect.get_collide(platform):
                if self.change_y > 0:
                    self.rect.bottom = platform.top
                elif self.change_y < 0:
                    self.rect.top = platform.bottom
                self.change_y = 0                

        # Teste si le player touche les bords du niveau
        if self.rect.right > SET.WINDOW_SIZE[0]:
            self.rect.right = SET.WINDOW_SIZE[0]
            self.toggle_walk = not self.toggle_walk
        if self.rect.left < 0:
            self.toggle_walk = not self.toggle_walk
            self.rect.left = 0

        if time.time() - self.chrono >= self.compteur:
            self.jump(random.randint(0,15))
            self.compteur = random.uniform(0,2)
            self.chrono = time.time()

    def calc_gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        if self.rect.bottom >= SET.WINDOW_SIZE[1] and self.change_y >= 0:
            self.change_y = 0
            self.rect.bottom = SET.WINDOW_SIZE[1]

    def jump(self, power=10):
        _jump = False
        self.rect.y += 2
        for platform in self.level.allPlatform["Platform"]:
            if self.rect.get_collide(platform):
                _jump = True
        self.rect.y -= 2
        if _jump or self.rect.bottom >= SET.WINDOW_SIZE[1]:
            self.change_y = -power

    def go_left(self):
        self.change_x = -9

    def go_right(self):
        self.change_x = 9

    def stop(self):
        self.change_x = 0

    def draw(self):
        self.rect.draw()

class Player:
    def __init__(self, level, pos=(10,10), size=(50,50)):
        self.rect = Rect(pos,size)
        self.change_x, self.change_y = 0, 0
        self.level = level

    def update(self):
        self.calc_gravity()
        self.rect.x += self.change_x

        for platform in self.level.allPlatform["Platform"]:
            if self.rect.get_collide(platform):
                if self.change_x > 0:
                    self.rect.right = platform.left
                elif self.change_x < 0:
                    self.rect.left = platform.right
                self.change_y = -2

        self.rect.y += self.change_y

        for platform in self.level.allPlatform["Platform"]:
            if self.rect.get_collide(platform):
                if self.change_y > 0:
                    self.rect.bottom = platform.top
                elif self.change_y < 0:
                    self.rect.top = platform.bottom
                self.change_y = 0                

        # If player touch the border
        if self.rect.right > SET.WINDOW_SIZE[0]:
            self.rect.right = SET.WINDOW_SIZE[0]
        if self.rect.left < 0:
            self.rect.left = 0

        for mob in Mob.Mob["Puce"]:
            if self.rect.get_collide(mob.rect):
                Mob.Mob["Puce"].remove(mob)
                Mob._score()


    def calc_gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        if self.rect.bottom >= SET.WINDOW_SIZE[1] and self.change_y >= 0:
            self.change_y = 0
            self.rect.bottom = SET.WINDOW_SIZE[1]

    def player_event(self, e):
        if e.type == 'keydown':
            if e.keyCode == 37 or e.keyCode == 81:
                self.go_left()
            if e.keyCode == 39 or e.keyCode == 68:
                self.go_right()
            if e.keyCode == 38 or e.keyCode == 90:
                self.jump()
        if e.type == 'keyup':
            if (e.keyCode == 37 or e.keyCode == 81) and self.change_x < 0:
                self.stop()
            if (e.keyCode == 39 or e.keyCode == 68) and self.change_x > 0:
                self.stop()
            if e.keyCode == 80:
                Mob.Mob["Puce"].append(Puce(self.level, (random.randint(0,SET.WINDOW_SIZE[0]),random.randint(0,SET.WINDOW_SIZE[1]))))

    def jump(self):
        _jump = False
        self.rect.y += 2
        for platform in self.level.allPlatform["Platform"]:
            if self.rect.get_collide(platform):
                _jump = True
        self.rect.y -= 2
        if _jump or self.rect.bottom >= SET.WINDOW_SIZE[1]:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

    def draw(self):
        self.rect.draw()

class Mob:
    Mob = {'Puce': list()}
    score = 0
    def update(name):
        for e in Mob.Mob[name]:
            e.update()
    def draw(name):
        for e in Mob.Mob[name]:
            e.draw()
    def _score():
        Mob.score += 1
        s = "Score : %s" % Mob.score
        doc["score"].text = s

def main(i):
    def animate(i):
        global id
        id = raf(animate)
        draw()

    def draw():
        Game.context.clearRect(0, 0, Game.canvas.width, Game.canvas.height)
        lvl.draw()
        Mob.update('Puce')
        player.update()
        Mob.draw('Puce')
        player.draw()

    global p
    p.style = {'display': "none"}

    Game.canvas = html.CANVAS(width=SET.WINDOW_SIZE[0], height=SET.WINDOW_SIZE[1])
    mL = (doc.body.clientWidth - SET.WINDOW_SIZE[0]) / 2
    Game.canvas.style = {"border": "1px solid black", 'marginLeft': "{}px".format(mL)}
    Game.context = Game.canvas.getContext("2d")

    if not Game.canvas:
        alert("Can't access to the canvas")
    Game.context = Game.canvas.getContext('2d')
    if not Game.context:
        alert("Can't access to the canvas")
    lvl = Level()
    player = Player(lvl)
    doc.body.addEventListener("keydown", player.player_event)
    doc.body.addEventListener("keyup", player.player_event)

    animate(0)

    doc.body.append(Game.canvas)

p = html.P(id="anim")
b = html.BUTTON('START')
b.style = {
    'width': "100%", 
    'height': '100%', 
    'fontFamily': 'sans-serif', 
    'fontSize': '60px', 
    'cursor': 'pointer'
}
p <= b
doc.body <= p
score = html.P(id="score")
doc.body <= score
doc["anim"].bind('click', main)
