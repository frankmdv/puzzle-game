import numpy as np
from puzzlight import a_star, Puzzle

def main_solve(initial_status, final_status=np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])):
    return a_star(Puzzle(initial_status), Puzzle(final_status))
