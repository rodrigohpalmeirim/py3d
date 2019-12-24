from graphics import GraphWin, Point, Line
from math import sin, cos, tan, radians

field_of_view = radians(45)

class Solid:
    def __init__(self, vertices, connections):
        self.vertices = vertices
        self.connections = connections
        self.items = []

    def draw(self, window, color="gray", width=1, update=True):
        focal_length = (min(window.getHeight(), window.getWidth())/2) / tan(field_of_view/2)
        window_width, window_height = window.getWidth(), window.getHeight()
        for c in self.connections:
            x1, y1, z1 = self.vertices[c[0]]
            x2, y2, z2 = self.vertices[c[1]]
            screen_x1 = (x1-(window_width/2)) * focal_length/z1 + (window_width/2)
            screen_y1 = (y1-(window_height/2)) * focal_length/z1 + (window_height/2)
            screen_x2 = (x2-(window_width/2)) * focal_length/z2 + (window_width/2)
            screen_y2 = (y2-(window_height/2)) * focal_length/z2 + (window_height/2)
            l = Line(Point(screen_x1, screen_y1), Point(screen_x2, screen_y2))
            l.draw(window)
            l.setOutline(color)
            l.setWidth(width)
            self.items.append(l)
        if update:
            window.update()
    
    def undraw(self):
        for item in self.items[:]:
            item.undraw()
            self.items.remove(item)
    
    def move(self, x, y=0, z=0):
        for key, vertex in self.vertices.items():
            vertex[0] += x
            vertex[1] += y
            vertex[2] += z
    
    def rotate(self, center, angle_x, angle_y=0, angle_z=0):
        for key, vertex in self.vertices.items():
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            vertex[1] = center[1] + vector[1]*cos(angle_x) - vector[2]*sin(angle_x)
            vertex[2] = center[2] + vector[1]*sin(angle_x) + vector[2]*cos(angle_x)
            
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            vertex[0] = center[0] + vector[0]*cos(angle_y) - vector[2]*sin(angle_y)
            vertex[2] = center[2] + vector[0]*sin(angle_y) + vector[2]*cos(angle_y)
            
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            vertex[0] = center[0] + vector[0]*cos(angle_z) - vector[1]*sin(angle_z)
            vertex[1] = center[1] + vector[0]*sin(angle_z) + vector[1]*cos(angle_z)
    
    def scale(self, center, scale_x, scale_y=0, scale_z=0):
        for key, vertex in self.vertices:
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            vertex[0] = center[0] + vector[0]*scale_x
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            vertex[1] = center[1] + vector[1]*scale_y
            vector = [vertex[0]-center[0], vertex[1]-center[1], vertex[2]-center[2]]
            vertex[2] = center[2] + vector[2]*scale_z

    def center(self):
        x = sum(vertex[0] for key, vertex in self.vertices.items()) / len(self.vertices)
        y = sum(vertex[1] for key, vertex in self.vertices.items()) / len(self.vertices)
        z = sum(vertex[2] for key, vertex in self.vertices.items()) / len(self.vertices)
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