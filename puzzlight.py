import numpy as np
from sortedcontainers import SortedListWithKey

# Exceptions

class NotSolvable(Exception):
    def __init__(self, message):
        self.message = message

# Functions

def is_solvable(puzzle):
    def count_inversions():
        num_list = [num for num in puzzle.flatten() if num != 0]
        len_list = len(num_list)
        count = 0

        for i in range(0, len_list - 1):
            for j in range(i + 1, len_list):
                if num_list[i] > num_list[j]:
                    count += 1

        return count

    return count_inversions() % 2 != 0


def manhattan_dist(current_puzzle, final_puzzle):
    distance = 0
    for num in range(0, 9):
        curr_col, curr_row = current_puzzle.index(num)
        final_col, final_row = final_puzzle.index(num)

        distance += abs(curr_col - final_col) + abs(curr_row - final_row)

    return distance


def a_star(initial_puzzle, final_puzzle):
    open_puzzles = SortedList([(0, initial_puzzle)], key=lambda x: x[0])
    closed_puzzles = set()

    try:
        if not is_solvable(initial_puzzle):
            raise NotSolvable('This puzzle is not solvable')

        while open_puzzles:
            current_puzzle = open_puzzles.get(0)

            if current_puzzle == final_puzzle:
                break

            open_puzzles.pop(0)

            for child_puzzle in current_puzzle.expand():
                if not child_puzzle in closed_puzzles:
                    f = manhattan_dist(child_puzzle, final_puzzle) + child_puzzle.level
                    open_puzzles.add((f, child_puzzle))
            closed_puzzles.add(current_puzzle)

    except NotSolvable as nt:
        print(nt)

    return open_puzzles, closed_puzzles


# Models 

class SortedList(SortedListWithKey):

    def get(self, index):
        return self._lists[0][index][1]


    def __getitem__(self, index):
        return self._lists[0][index][1].table


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


    def __init__(self, table, movement=None, level=0):
        self.table = table
        self.movement = movement
        self.level = level


    def __eq__(self, obj):
        return (isinstance(obj, Puzzle) and np.array_equal(self.table, obj.table))


    def __hash__(self):
        return hash(self.table.tobytes())


    def __str__(self):
        return str(self.table)


    def __getitem__(self, index):
        row, col = index
        return self.table[row, col]


    def __setitem__(self, index, value):
        row, col = index
        self.table[row, col] = value

    
    def flatten(self):
        return self.table.flatten()


    def index(self, num):
        row, column = np.where(self.table == num)
        return row[0], column[0]


    def move_empty(self, movement, value_movement):
        row, column = self.index(0)
        row_value, column_value = value_movement
        row_movement, column_movement = row + row_value, column + column_value

        if 0 <= row_movement < 3 and 0 <= column_movement < 3:
            new_table = self.table.copy()
            new_table[row, column], new_table[row_movement, column_movement] = new_table[row_movement, column_movement], new_table[row, column]

            return Puzzle(new_table, movement, self.level + 1)

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
