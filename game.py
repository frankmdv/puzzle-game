from models import Puzzle, Node, Tree
import time

initial_puzzle = Puzzle([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]])

target_puzzle = Puzzle([[8, 7, 6],
                        [5, 4, 3],
                        [2, 1, 0]])

tree = Tree(Node(initial_puzzle))

start_time = time.time()
result = tree.BFS(target_puzzle)
end_time = time.time()

result_time = end_time - start_time
print(result.puzzle)
print(result_time)
