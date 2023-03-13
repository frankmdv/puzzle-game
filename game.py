import numpy as np
from puzzlight import breadth_search, a_star, Puzzle
import time

def main_solve(initial_status, final_status=np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])):
    return a_star(Puzzle(initial_status), Puzzle(final_status))


def second_solve(initial_status, final_status=np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])):
    return breadth_search(Puzzle(initial_status), Puzzle(final_status))

# Las dos matrices deben ser impares.

initial_status = np.array([[3, 4, 6],
                           [7, 8, 0],
                           [1, 2, 5]])

final_status = np.array([[1, 2, 3],
                         [8, 0, 4],
                         [7, 6, 5]])

first_start_t = time.time()
second_solve(initial_status, final_status)
first_end_t = time.time()
print('BFS algorithm:', first_end_t - first_start_t)


second_start_t = time.time()
main_solve(initial_status, final_status)
second_end_t = time.time()
print('a_star algorithm:', second_end_t - second_start_t)
