from graphics import GraphWin, Point, Line
from math import sin, cos, radians
from time import sleep

class Solid:
    def __init__(self, vertices, connections):
        self.vertices = vertices
        self.connections = connections

    def draw(self, window, color="gray"):
        for c in self.connections:
            l = Line(Point(self.vertices[c[0]][0], self.vertices[c[0]][1]), Point(self.vertices[c[1]][0], self.vertices[c[1]][1]))
            l.draw(window)
            l.setOutline(color)
        window.update()
    
    def move(self, x, y=0, z=0):
        for key, vertex in self.vertices.items():
            vertex[0] += x
            vertex[1] += y
            vertex[2] += z
    
    def rotate(self, center, axis, angle):
        for key, vertex in self.vertices.items():
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            if axis == "x":
                vertex[1] = center[1] + vector[1]*cos(angle) - vector[2]*sin(angle)
                vertex[2] = center[2] + vector[1]*sin(angle) + vector[2]*cos(angle)
            if axis == "y":
                vertex[0] = center[0] + vector[0]*cos(angle) - vector[2]*sin(angle)
                vertex[2] = center[2] + vector[0]*sin(angle) + vector[2]*cos(angle)
            if axis == "z":
                vertex[0] = center[0] + vector[0]*cos(angle) - vector[1]*sin(angle)
                vertex[1] = center[1] + vector[0]*sin(angle) + vector[1]*cos(angle)
    
    def scale(self, center, axis, scale):
        for key, vertex in self.vertices.items():
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            if axis == "x":
                vertex[0] = center[0] + vector[0]*scale
            if axis == "y":
                vertex[1] = center[1] + vector[1]*scale
            if axis == "z":
                vertex[2] = center[2] + vector[2]*scale

    def center(self):
        x = sum(vertex[0] for key, vertex in self.vertices.items())/len(self.vertices)
        y = sum(vertex[1] for key, vertex in self.vertices.items())/len(self.vertices)
        z = sum(vertex[2] for key, vertex in self.vertices.items())/len(self.vertices)
        return (x, y, z)


def merge(obj1, obj2):
    vertices = {}
    connections = []
    for key, vertex in obj1.vertices.items():
        vertices["1_"+str(key)] = vertex
    for key, vertex in obj2.vertices.items():
        vertices["2_"+str(key)] = vertex
    for c in obj1.connections:
        connections.append(["1_"+str(c[0]), "1_"+str(c[1])])
    for c in obj2.connections:
        connections.append(["2_"+str(c[0]), "2_"+str(c[1])])
    return Solid(vertices, connections)


def clear(window):
    for item in window.items[:]:
        item.undraw()