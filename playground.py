from engine import *
import random, sys, time
from math import pi
from graphics import Text

w = GraphWin("Test", 800, 600, autoflush=False)
w.setBackground("black")

def clear(window, update=True):
    for item in window.items[:]:
        item.undraw()

quit = False
paused = False

def pause():
    global paused
    if not paused:
        paused = True
    else:
        paused = False

def keypress(event):
    global quit
    if event.char == "q":
        quit = True
    elif event.char == "p":
        pause()

w.focus_set()
w.bind('<Key>', keypress)

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

grid_spacing = w.getWidth()//10
grid_size = 2*w.getWidth()

grid_points = {}
grid_connections = []
for i, pos in enumerate(range(0, grid_size+1, grid_spacing)):
    index = i*4
    grid_points[index] = [w.getWidth()//2-grid_size//2+pos, w.getHeight(), 0]
    grid_points[index+1] = [w.getWidth()//2-grid_size//2+pos, w.getHeight(), grid_size]
    grid_points[index+2] = [w.getWidth()//2-grid_size//2, w.getHeight(), pos]
    grid_points[index+3] = [w.getWidth()//2+grid_size//2, w.getHeight(), pos]
    grid_connections += [[index, index+1], [index+2, index+3]]

grid = Solid(grid_points, grid_connections)

grid.move(0, 0, 1)

grid.draw(w, "gray")

thing = cube
thing.move(w.getWidth()//2-50, w.getHeight()//2-50, 150)

rand1 = random.random()*2*pi
rand2 = random.random()*2*pi
rand3 = random.random()*2*pi

start_time = time.time()
last_time = start_time
last_tick_durations = []

max_fps = 60

i = 0
while True:

    tick_duration = time.time()-last_time
    
    if tick_duration < 1/max_fps:
        time.sleep(1/max_fps - tick_duration)
        tick_duration = time.time()-last_time

    last_time = time.time()
    last_tick_durations.insert(0, tick_duration)
    try: last_tick_durations.pop(19)
    except: pass

    if w.isClosed() or quit:
        sys.exit()

    if paused:
        time.sleep(0.05)
        w.update()
        continue

    clear(w, update=False)
    thing.rotate(thing.center(), "x", tick_duration*sin(i*0.01*(rand1/4)+rand2)*2)
    thing.rotate(thing.center(), "z", tick_duration*sin(i*0.01*(rand2/4)+rand3)*2)
    thing.rotate(thing.center(), "y", tick_duration*sin(i*0.01*(rand3/4)+rand1)*2)
    
    grid.draw(w, width=2, update=False)
    thing.draw(w, "white", width=3, update=False)
    
    fps = Text(Point(20, 15), round(1/(sum(last_tick_durations)/len(last_tick_durations)), 1))
    fps.setTextColor("white")
    fps.draw(w)
    w.update()
    fps.undraw()

    i += 1

w.getMouse()