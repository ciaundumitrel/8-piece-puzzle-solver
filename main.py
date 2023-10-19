
from puzzle import Puzzle
from solver import iddfs

if __name__ == '__main__':

    puzzle = Puzzle([[8, 6, 7],
                     [2, 5, 4],
                     [0, 3, 1]])

    puzzle = Puzzle([[2, 7, 5],
                     [9, 4, 3],
                     [1, 6, 0]])

    puzzle = Puzzle([[2, 5, 3], [1, 0, 6], [4, 7, 8]])


    puzzle = Puzzle([[2, 7, 5],
                     [0, 8, 4],
                     [3, 1, 6]])

    puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [8, 7, 0]])

    iddfs(puzzle, 31)
