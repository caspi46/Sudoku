# from https://lvngd.com/blog/generating-and-solving-sudoku-puzzles-python/

import random
import copy
class SudokuSetSet:
    def __init__(self, grid=None):
        self.counter = 0
        # path is for the matplotlib animation
        #self.path = []
        # if a grid/puzzle is passed in, make a copy and solve it
        if grid:
            if len(grid[0]) == 9 and len(grid) == 9:
                self.grid = grid
                self.original = copy.deepcopy(grid)
                self.solve_input_sudoku()
            else:
                print("input needs to be a 9x9 matrix")
        else:
            # if no puzzle is passed, generate one
            self.grid = [[0 for i in range(9)] for j in range(9)]
            self.generate_puzzle()
            self.original = copy.deepcopy(self.grid)

    def solve_input_sudoku(self):
        """solves a puzzle"""
        self.generate_solution(self.grid)
        return
    def num_used_in_row(self, grid, row, number):
        """returns True if the number has been used in that row"""
        if number in grid[row]:
            return True
        return False

    def num_used_in_column(self, grid, col, number):
        """returns True if the number has been used in that column"""
        for i in range(9):
            if grid[i][col] == number:
                return True
        return False

    def num_used_in_subgrid(self, grid, row, col, number):
        """returns True if the number has been used in that subgrid/box"""
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, (sub_row + 3)):
            for j in range(sub_col, (sub_col + 3)):
                if grid[i][j] == number:
                    return True
        return False
    def generate_solution(self, grid):
        """generates a full solution with backtracking"""
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            # find next empty cell
            if grid[row][col] == 0:
                random.shuffle(number_list)
                for number in number_list:
                    if self.valid_location(grid, row, col, number):
                        #self.path.append((number, row, col))
                        grid[row][col] = number
                        if self.find_empty_square(grid):
                            return True
                        else:
                            if self.generate_solution(grid):
                                # if the grid is full
                                return True
                break
        grid[row][col] = 0
        return False

    def valid_location(self, grid, row, col, number):
        if self.num_used_in_row(grid, row, number):
            return False
        if self.num_used_in_column(grid, col, number):
            return False
        if self.num_used_in_subgrid(grid, row, col, number):
            return False
        return True

    def find_empty_square(self, grid):
        for i in range(9):
            if not all(element != 0 for element in grid[i]):
                return False
        return True

    def print_grid(self, grid_name=None):
        if grid_name:
            print(grid_name)
        for row in self.grid:
            print(row)
        return
