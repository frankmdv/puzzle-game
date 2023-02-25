from collections import deque
import numpy as np

class Tree:
    def __init__(self, root):
        self.root = root


    def BFS(self, target_node):
        pending_nodes = deque([self.root])
        visited_nodes = { self.root }

        while pending_nodes:
            current_node = pending_nodes.popleft()

            if current_node == target_node:
                return current_node

            for node in current_node.expand():
                if not node in visited_nodes:
                    pending_nodes.append(node)
                    visited_nodes.add(node)


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent 


    def __eq__(self, obj):
        return (isinstance(obj, Node) and np.array_equal(self.data.matrix, obj.data.matrix)) or \
               (isinstance(obj, Puzzle) and np.array_equal(self.data.matrix, obj.matrix)) 


    def __hash__(self):
        return hash(self.data.matrix.tobytes())


    def expand(self):
        children = []

        for movement in Puzzle.MOVEMENTS:
            value_movement = Puzzle.MOVEMENTS[movement]['VALUE']
            inverse_movement = None

            if not self.data.movement is None:
                inverse_movement = Puzzle.MOVEMENTS[self.data.movement]['INVERSE']

            if not movement == inverse_movement:
                child = self.data.move_cell(movement, value_movement)

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


    def get_pos_cell(self, token):
        row, column = np.where(self.matrix == token)
        return row[0], column[0]


    def move_cell(self, movement, value_movement):
        row, column = self.get_pos_cell(0)
        n_rows, n_columns = self.matrix.shape
        row_value, column_value = value_movement
        row_movement, column_movement = row + row_value, column + column_value

        if 0 <= row_movement < n_rows and 0 <= column_movement < n_columns:
            new_matrix = self.matrix.copy()
            new_matrix[row][column], new_matrix[row_movement][column_movement] = new_matrix[row_movement][column_movement], new_matrix[row][column]

            return Puzzle(new_matrix, movement)

        return None
