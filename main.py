from pprint import pprint

from puzzle import Puzzle
from solver import iddfs, greedy

if __name__ == '__main__':

    puzzle = Puzzle([[8, 6, 7], [2, 5, 4], [0, 3, 1]])
    #
    # iddfs(puzzle, max_depth=31)

    # puzzle = Puzzle([[2, 5, 3], [1, 0, 6], [4, 7, 8]])
    #
    # iddfs(puzzle, max_depth=31)

    puzzle = Puzzle([[2, 7, 5], [0, 8, 4], [3, 1, 6]])
    #
    # iddfs(puzzle, max_depth=31)

    # Invalid input
    # puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [8, 7, 0]])
    # iddfs(puzzle, max_depth=31)

    pprint(greedy(puzzle))
