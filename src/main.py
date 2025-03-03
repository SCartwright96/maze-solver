from graphics import Line, Window, Point, Cell
from maze import Maze
import time
import sys
sys.setrecursionlimit(10000)
import random

WIDTH = 2000
HEIGHT = 1500



def main():
    win = Window(WIDTH,HEIGHT)
    '''
    line = Line(Point(20, 80), Point(190, 680))
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.has_bottom_wall = False
    cell1.draw(20,40,40,20)
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_top_wall = False
    cell2.draw(40,20,60,40)
    cell1.draw_move(cell2)
    '''
    while True:
        cols = random.randrange(10,101)
        rows = random.randrange(10,101)
        scale = min((HEIGHT-20)/rows, (WIDTH-20)/cols)

        
        cur_maze = Maze(10,10,rows,cols,scale,scale,win)

        print (cur_maze.solve())

        time.sleep(3)
        win.canvas.delete("all")
        del cur_maze

        

        
    win.wait_for_close()
main()