from graphics import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(0,0)
        self._draw_cell(self.num_cols-1 , self.num_rows-1)

        
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                
                self._draw_cell(i,j)

    def _draw_cell(self, col, row):
        if self._cells[col][row] == None:
            self._cells[col][row] = Cell(self.win)
        x_dist_modified = self.cell_size_x*col+self.x1
        y_dist_modified = self.cell_size_y*row+self.y1
        self._cells[col][row].draw(x_dist_modified, y_dist_modified, x_dist_modified+self.cell_size_x, y_dist_modified+self.cell_size_y)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)

