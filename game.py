import numpy as np
from models import Puzzle, Search
import time

initial_puzzle = Puzzle([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]])

target_puzzle = Puzzle([[8, 7, 6],
                        [5, 4, 3],
                        [2, 1, 0]])

print(initial_puzzle.expand())


def main_solve(initial_status, final_status=np.array([[1, 2, 3], [8, 0, 4], [7, 6 ,5]])):
    return Search.a_star(initial_status, final_status)
