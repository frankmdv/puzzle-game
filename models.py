from heapdict import heapdict
from collections import deque
import numpy as np
import time 

class Heuristics:
    @staticmethod
    def calc_manhattan_dist(initial_puzzle, target_puzzle):
        def manhattan_dist(col1, row1, col2, row2):
            return abs(col1 - col2) + abs(row1 - row2)

        num_rows, num_columns = initial_puzzle.matrix.shape
        matrix_size = num_rows * num_columns
        distance = 0

        for num in range(0, matrix_size):
            col1, row1 = initial_puzzle.get_pos_num(num)
            col2, row2 = target_puzzle.get_pos_num(num)

            distance += manhattan_dist(col1, row1, col2, row2)

        return distance


class Search:
    @staticmethod
    def a_star(initial_status, final_status):
        pass


    @staticmethod
    def breadth_search(initial_status, final_status):
       open_states = deque([initial_status])
       closed_states = set()

       while open_states:
           current_array = open_states.popleft()

           if current_array == final_status:
               return current_array

           closed_states.add(current_array)


           for array in current_array.expand():
               if not array in closed_states:
                   open_states.append(array)
                   closed_states.add(array)


class Puzzle:
    MOVEMENTS = {
        'UP': {
            'VALUE': (-1, 0),
            'INVERSE': 'DOWN'
        },
        'DOWN': {
            'VALUE': (1, 0),
            'INVERSE': 'UP'
        },
        'RIGHT': {
            'VALUE': (0, 1),
            'INVERSE': 'LEFT'
        },
        'LEFT': {
            'VALUE': (0, -1),
            'INVERSE': 'RIGHT'
        }
    }


    def __init__(self, table, movement=None):
        self.table = table
        self.movement = movement


    def __eq__(self, puzzle):
        return isinstance(puzzle, Puzzle) and np.array_equal(self.table, puzzle.table)


    def __hash__(self):
        return hash(self.table.tobytes())


    def get_pos_num(self, num):
        row, column = np.where(self.table == num)
        return row[0], column[0]


    def move_empty(self, movement, value_movement):
        row, column = self.get_pos_num(0)
        n_rows, n_columns = self.table.shape
        row_value, column_value = value_movement
        row_movement, column_movement = row + row_value, column + column_value

        if 0 <= row_movement < n_rows and 0 <= column_movement < n_columns:
            new_table = self.table.copy()
            new_table[row, column], new_table[row_movement, column_movement] = new_table[row_movement, column_movement], new_table[row, column]

            return Puzzle(new_table, movement)

        return None


    def expand(self):
        children = []

        for movement in Puzzle.MOVEMENTS:
            value_movement = Puzzle.MOVEMENTS[movement]['VALUE']
            inverse_movement = None

            if not self.movement is None:
                inverse_movement = Puzzle.MOVEMENTS[self.movement]['INVERSE']

            if not movement == inverse_movement:
                child = self.move_empty(movement, value_movement)

                if not child is None:
                    children.append(child)

        return children
