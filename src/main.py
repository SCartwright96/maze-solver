from graphics import Line, Window, Point, Cell
from maze import Maze

def main():
    win = Window(1920,1080)
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
    
    cur_maze = Maze(20,20,10,10,60,60,win)

    win.wait_for_close()
main()