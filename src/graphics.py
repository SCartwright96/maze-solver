from tkinter import Tk, BOTH, Canvas
import random
from colors import BACKGROUND_COLOR, FAIL_COLOR, PASS_COLOR, WALL_COLOR

class Window():
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root_widget, bg=BACKGROUND_COLOR, height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell, fill_color = "black"):
        cell.draw(self.canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width = 2
            )
           
class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = min(x1,x2)
        self._x2 = max(x1,x2)
        self._y1 = min(y1,y2)
        self._y2 = max(y1,y2)

        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, WALL_COLOR if self.has_left_wall else BACKGROUND_COLOR)
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, WALL_COLOR if self.has_top_wall else BACKGROUND_COLOR)
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, WALL_COLOR if self.has_right_wall else BACKGROUND_COLOR)
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, WALL_COLOR if self.has_bottom_wall else BACKGROUND_COLOR)

        '''if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)'''

    def draw_move(self, to_cell, undo = False, undo_color = FAIL_COLOR):
        if undo:
            line_color = undo_color
        else:
            line_color = PASS_COLOR
        
        center1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) /2)
        center2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) /2)
        self._win.draw_line(Line(center1, center2), line_color) 