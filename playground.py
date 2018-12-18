from engine import *
import random
from math import pi

w = GraphWin("Test", 500, 500, autoflush=False)
w.setBackground("black")

cube = Solid({
    1: [0, 0, 0],
    2: [100, 0, 0],
    3: [100, 100, 0],
    4: [0, 100, 0],
    5: [0, 0, 100],
    6: [100, 0, 100],
    7: [100, 100, 100],
    8: [0, 100, 100],
}, [
    [1, 2], [2, 3], [3, 4], [4, 1],
    [5, 6], [6, 7], [7, 8], [8, 5],
    [1, 5], [2, 6], [3, 7], [4, 8]
    ])

piramid = Solid({
    1: [0, 0, 0],
    2: [100, 0, 0],
    3: [100, 100, 0],
    4: [0, 100, 0],
    5: [50, 50, 100]
}, [
    [1, 2], [2, 3], [3, 4], [4, 1],
    [1, 5], [2, 5], [3, 5], [4, 5],
])

T = Solid({
    1: [50, 0, 0],
    2: [50, 25, 0],
    3: [75, 25, 0],
    4: [75, 0, 0],
    5: [50, 0, 100],
    6: [50, 25, 100],
    7: [75, 25, 100],
    8: [75, 0, 100],
    9: [0, 0, 100],
    10: [0, 25, 100],
    11: [125, 25, 100],
    12: [125, 0, 100],
    13: [0, 0, 125],
    14: [0, 25, 125],
    15: [125, 25, 125],
    16: [125, 0, 125],
}, [
    [1, 2], [2, 3], [3, 4], [4, 1],
    [1, 5], [2, 6], [3, 7], [4, 8],
    [5, 9], [6, 10], [7, 11], [8, 12], [5, 6], [7, 8], [9, 10], [11, 12],
    [9, 13], [10, 14], [11, 15], [12, 16],
    [13, 14], [14, 15], [15, 16], [16, 13]
])

thing = cube
thing.move(200, 200, 200)

thing.draw(w)

rand1 = random.random()*2*pi
rand2 = random.random()*2*pi
rand3 = random.random()*2*pi

for i in range(10000):
    clear(w)
    thing.rotate(thing.center(), "x", radians(sin(i/100*(rand1/4)+rand2)*2))
    thing.rotate(thing.center(), "z", radians(sin(i/100*(rand2/4)+rand3)*2))
    thing.rotate(thing.center(), "y", radians(sin(i/100*(rand3/4)+rand1)*2))
    thing.rotate((250, 250, 50), "z", radians(0))
    thing.draw(w, "white")
    sleep(0.01)

w.getMouse()