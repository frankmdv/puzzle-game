import numpy as np
from models import Puzzle, Search
import time

def main_solve(initial_status, final_status=Puzzle(np.array([[1, 2, 3], [8, 0, 4], [7, 6 ,5]]))):
    return Search.breadth_search(initial_status, final_status)


initial_status = Puzzle(np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 0]]))

final_status = Puzzle(np.array([[8, 7, 6],
                                [5, 4, 3],
                                [2, 1, 0]]))

start_time = time.time()
print(main_solve(initial_status, final_status).table)
end_time = time.time()

print(end_time - start_time)
