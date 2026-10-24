# Description

A small wireframe 3D engine written in Python. It was mostly an experiment I worked on while learning about linear algebra, computer graphics and Python. It uses John Zelle's [`graphics.py`](https://mcsp.wartburg.edu/zelle/python/graphics.py) library, which is bundled in this repo and runs on Tkinter.

Objects are defined as a `Solid`: a set of vertices plus the edges that connect them. A `Solid` can be moved, rotated around a point and merged with other solids. It is drawn with a simple perspective projection using a 45° field of view.

`playground.py` defines a few example solids: a cube, a pyramid, a "T", an octahedron and a dodecahedron. It draws a perspective floor grid and spins the dodecahedron with randomized rotation speeds, capped at 60 FPS, with an FPS counter.

# Usage
Requires Python 3 with Tkinter. There are no other dependencies.
```sh
python3 playground.py
```

# Controls
- `p`: pause/resume
- `q`: quit
