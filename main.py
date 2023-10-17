import sys

from puzzle import Puzzle
from solver import iddfs

if __name__ == '__main__':

    puzzle = Puzzle([[8, 6, 7],
                     [2, 5, 4],
                     [0, 3, 1]])

    # 4 depth

    # 16
    puzzle = Puzzle([[2, 7, 5],
                     [8, 4, 3],
                     [1, 6, 0]])


    # 21 depth
    puzzle = Puzzle([[2, 7, 5],
                     [0, 8, 4],
                     [3, 1, 6]])

    iddfs(puzzle, 31)

    puzzle = Puzzle([[2, 5, 3], [1, 0, 6], [4, 7, 8]])
