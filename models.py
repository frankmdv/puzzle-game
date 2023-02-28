from heapdict import heapdict
from collections import deque
import numpy as np

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


class Tree:
    def __init__(self, root):
        self.root = root


    def BFS(self, target_puzzle):
        pending_nodes = deque([self.root])
        visited_nodes = { self.root }

        while pending_nodes:
            current_node = pending_nodes.popleft()

            if current_node == target_puzzle:
                return current_node

            for node in current_node.expand():
                if not node in visited_nodes:
                    pending_nodes.append(node)
                    visited_nodes.add(node)


    def find(self, target_puzzle):
        pass



class Node:
    def __init__(self, puzzle, parent=None):
        self.puzzle = puzzle
        self.parent = parent 


    def __eq__(self, obj):
        return (isinstance(obj, Node) and np.array_equal(self.puzzle.matrix, obj.puzzle.matrix)) or \
               (isinstance(obj, Puzzle) and np.array_equal(self.puzzle.matrix, obj.matrix)) 


    def __hash__(self):
        return hash(self.puzzle.matrix.tobytes())


    def expand(self):
        children = []

        for movement in Puzzle.MOVEMENTS:
            value_movement = Puzzle.MOVEMENTS[movement]['VALUE']
            inverse_movement = None

            if not self.puzzle.movement is None:
                inverse_movement = Puzzle.MOVEMENTS[self.puzzle.movement]['INVERSE']

            if not movement == inverse_movement:
                child = self.puzzle.move_empty(movement, value_movement)

                if not child is None:
                    children.append(Node(child, self))

        return children


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


    def __init__(self, matrix, movement=None):
        self.matrix = np.array(matrix)
        self.movement = movement 


    def __str__(self):
        return str(self.matrix)


    def get_pos_num(self, num):
        row, column = np.where(self.matrix == num)
        return row[0], column[0]


    def move_empty(self, movement, value_movement):
        row, column = self.get_pos_num(0)
        n_rows, n_columns = self.matrix.shape
        row_value, column_value = value_movement
        row_movement, column_movement = row + row_value, column + column_value

        if 0 <= row_movement < n_rows and 0 <= column_movement < n_columns:
            new_matrix = self.matrix.copy()
            new_matrix[row, column], new_matrix[row_movement, column_movement] = new_matrix[row_movement, column_movement], new_matrix[row, column]

            return Puzzle(new_matrix, movement)

        return None
