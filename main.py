import sys
import random
import time

try:
    import bext, colorama
except ImportError:
    print('Для запуска программы нужны модули bext и colorama.')
    sys.exit ()

class Drop:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = -1
        self.drop_type = random.randint(0, 1)
        self.timeout = random.randint(0, 3)
        self.wait_count = random.randint(0, 3)
    def renew(self):
        self.__init__()
    def move(self):
        if drop.wait_count < drop.timeout:
            drop.wait_count += 1
            return False
        else:
            drop.wait_count = 0
            drop.y += 1
            return True
    def draw(self):
        if self.drop_type == 1:
            symbol = str(random.randint(1, 9))
            con_print(self.x, self.y, green, symbol)
            self.zero_draw()
        else:
            con_print(self.x, self.y, green, ' ')
    def zero_draw (self):
        if (self.y < height):
            con_print(self.x, self.y+1, lgreen, '0')

def is_rb_corner(x, y):
    if x == width and y == height:
        return True
    else:
        return False

def con_print(x, y, color, symbol):
    if not is_rb_corner(x, y):
        bext.goto(x, y)
        sys.stdout.write (color)
        print(symbol, end='')

bext.clear()
bext.hide()
width, height = bext.size()
width -= 1
height -= 1

green = colorama.Fore.GREEN
lgreen = colorama.Fore.LIGHTGREEN_EX


drops = []
for i in range(1, width*2//3):
    drop = Drop()
    drops.append(drop)

while True:
    for drop in drops:
        if drop.move():
            drop.draw()
            if drop.y >= height:
                drop.renew()
    key = bext.getKey(blocking = False)
    if key == 'esc':
        bext.clear()
        sys.exit()
    time.sleep(0.06)