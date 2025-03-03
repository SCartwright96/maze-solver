from graphics import Cell
import time
import random
from colors import FAIL_COLOR

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
        self.random_color = None
        self.first_sequential_fail = True

        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_visited_cells()
        


    def solve(self, speed = 0.05):
        return self._solve_r(0,0, speed)
    
    def _solve_r(self, i, j, speed = 0.05):
        print(f"Checking {i}, {j}")
        self._animate(speed)
        self._cells[i][j].visited = True
        if i == self.num_rows-1 and j == self.num_cols-1:
            return True
        
        

        if i+1<self.num_rows and not self._cells[i][j].has_bottom_wall and self._cells[i+1][j] and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            self.first_sequential_fail = True
            if self._solve_r(i+1,j,speed):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True, self.random_color)

        if j+1<=self.num_cols-1 and not self._cells[i][j].has_right_wall and self._cells[i][j+1] and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            self.first_sequential_fail = True
            if self._solve_r(i,j+1,speed):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True, self.random_color)

        if j-1>=0 and not self._cells[i][j].has_left_wall and self._cells[i][j-1] and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            self.first_sequential_fail = True
            if self._solve_r(i,j-1,speed):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True, self.random_color)

        if i-1 >= 0 and not self._cells[i][j].has_top_wall and self._cells[i-1][j] and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            self.first_sequential_fail = True
            if self._solve_r(i-1,j,speed):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True, self.random_color)

        

        if self.first_sequential_fail:
            self.random_color = FAIL_COLOR
            #self.random_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            self.first_sequential_fail = False
        return False
        

    def _reset_visited_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False


    def _break_walls_r(self, i, j):
        if self._cells[i][j].visited:
            return
        self._cells[i][j].visited = True
        while 1 == 1:
            
            up_possible = i-1>= 0 and self._cells[i-1][j] is not None and not self._cells[i-1][j].visited
            down_possible = i+1<self.num_rows and self._cells[i+1][j] is not None and not self._cells[i+1][j].visited
            left_possible = j-1 >= 0 and self._cells[i][j-1] is not None and not self._cells[i][j-1].visited
            right_possible = j+1<self.num_cols and self._cells[i][j+1] is not None and not self._cells[i][j+1].visited
            print(f'{i}, {j} up: {up_possible} down: {down_possible} left: {left_possible} right: {right_possible}')
            if not(up_possible or right_possible or down_possible or left_possible):
                self._draw_cell(i,j,0.0001)
                return

            match random.randrange(0,4):
                case 0:
                    if up_possible:
                        #print(f'Removing top wall from ({i}, {j}) and bottom wall from ({i-1}, {j})')
                        self._cells[i][j].has_top_wall = False
                        self._cells[i-1][j].has_bottom_wall = False
                        self._break_walls_r(i-1,j)
                case 1:
                    if down_possible:
                        #print(f'Removing bottom wall from ({i}, {j}) and top wall from ({i+1}, {j})')
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[i+1][j].has_top_wall = False
                        self._break_walls_r(i+1,j)
                case 2:
                    if left_possible:
                        #print(f'Removing left wall from ({i}, {j}) and right wall from ({i}, {j-1})')
                        self._cells[i][j].has_left_wall = False
                        self._cells[i][j-1].has_right_wall = False
                        self._break_walls_r(i,j-1)
                case 3:
                    if right_possible:
                        #print(f'Removing right wall from ({i}, {j}) and left wall from ({i}, {j+1})')
                        self._cells[i][j].has_right_wall = False
                        self._cells[i][j+1].has_left_wall = False
                        self._break_walls_r(i,j+1)
            #time.sleep(1)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[self.num_rows-1][self.num_cols-1].has_right_wall = False
        self._draw_cell(0,0)
        self._draw_cell(self.num_rows-1 , self.num_cols-1)

        
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                self._cells[i].append(Cell(self.win))
                
                self._draw_cell(i,j,0.0001)

    def _draw_cell(self, row, col, speed = 0.05):
        if self._cells[row][col] == None:
            self._cells[row][col] = Cell(self.win)
        x_dist_modified = self.cell_size_x*col+self.x1
        y_dist_modified = self.cell_size_y*row+self.y1
        self._cells[row][col].draw(x_dist_modified, y_dist_modified, x_dist_modified+self.cell_size_x, y_dist_modified+self.cell_size_y)

        self._animate(speed)

    def _animate(self, speed = 0.05):
        self.win.redraw()
        #time.sleep(speed)

