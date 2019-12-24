from engine import *
import random, sys, time
from math import pi, sqrt
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

octahedron = Solid({
    1: [50, 0, 0],
    2: [0, 50, 0],
    3: [0, 0, 50],
    4: [-50, 0, 0],
    5: [0, -50, 0],
    6: [0, 0, -50],
}, [
    [1, 2], [1, 3], [1, 5], [1, 6],
    [2, 3], [2, 4], [2, 6],
    [3, 4], [3, 5],
    [4, 5], [4, 6],
    [5, 6]
])

golden_ratio = (1+sqrt(5))/2

dodecahedron = Solid({
    1: [50, 50, 50],
    2: [50, 50, -50],
    3: [50, -50, 50],
    4: [50, -50, -50],
    5: [-50, 50, 50],
    6: [-50, 50, -50],
    7: [-50, -50, 50],
    8: [-50, -50, -50],
    9: [0, 50*golden_ratio, 50/golden_ratio],
    10: [0, 50*golden_ratio, -50/golden_ratio],
    11: [0, -50*golden_ratio, 50/golden_ratio],
    12: [0, -50*golden_ratio, -50/golden_ratio],
    13: [50/golden_ratio, 0, 50*golden_ratio],
    14: [50/golden_ratio, 0, -50*golden_ratio],
    15: [-50/golden_ratio, 0, 50*golden_ratio],
    16: [-50/golden_ratio, 0, -50*golden_ratio],
    17: [50*golden_ratio, 50/golden_ratio, 0],
    18: [50*golden_ratio, -50/golden_ratio, 0],
    19: [-50*golden_ratio, 50/golden_ratio, 0],
    20: [-50*golden_ratio, -50/golden_ratio, 0],
}, [
    [1, 9], [1, 13], [1, 17],
    [2, 10], [2, 14], [2, 17],
    [3, 11], [3, 13], [3, 18],
    [4, 12], [4, 14], [4, 18],
    [5, 9], [5, 15], [5, 19],
    [6, 10], [6, 16], [6, 19],
    [7, 11], [7, 15], [7, 20],
    [8, 12], [8, 16], [8, 20],
    [9, 10],
    [11, 12],
    [13, 15],
    [14, 16],
    [17, 18],
    [19, 20]
])

grid_spacing = w.getWidth()//10
grid_size = 3*w.getWidth()

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
grid.draw(w, "gray", width=2, update=False)

thing = dodecahedron
thing.move(w.getWidth()//2, w.getHeight()//2, 500)

rand1 = random.random()*2*pi
rand2 = random.random()*2*pi
rand3 = random.random()*2*pi

start_time = time.time()
last_time = start_time
last_tick_durations = []

max_fps = 60

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
        thing.draw(w, "white", width=3, update=False)
        w.update()
        thing.undraw()
        continue

    thing.rotate(thing.center(), tick_duration*sin(last_time*0.5*(rand1/4)+rand2)*2,
                                 tick_duration*sin(last_time*0.5*(rand2/4)+rand3)*2,
                                 tick_duration*sin(last_time*0.5*(rand3/4)+rand1)*2)
                                 
    thing.draw(w, "white", width=3, update=False)
    
    fps = Text(Point(20, 15), round(1/(sum(last_tick_durations)/len(last_tick_durations)), 1))
    fps.setTextColor("white")
    fps.draw(w)
    w.update()
    fps.undraw()
    thing.undraw()