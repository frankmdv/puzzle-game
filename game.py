import numpy as np
from models import Puzzle, Search
import time

def main_solve(initial_status, final_status=np.array([[1, 2, 3], [8, 0, 4], [7, 6 ,5]])):
    return Search.breadth_search(initial_status, final_status)


initial_status = Puzzle([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]])

final_status = Puzzle([[8, 7, 6],
                       [5, 4, 3],
                       [2, 1, 0]])

#print(initial_status.expand())
print(main_solve(initial_status, final_status))
