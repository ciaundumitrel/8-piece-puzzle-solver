import os
import subprocess

from puzzle import Puzzle


def get_hamming_distance(puzzle):
    return sum((puzzle.get_matrix_as_list().index(node) == puzzle.get_initial_matrix_as_list().index(node))
               for node in range(0, 9))


itr = 0


def iddfs(pz: Puzzle, max_depth: int = 40):
    iddfs_solution = []
    transitions = []
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def display_puzzle_transitions(transitions_):

        subprocess.call('clear' if os.name == 'posix' else 'cls')

        for i, state in enumerate(transitions_):
            for row in state:
                print(" ".join(map(str, row)))
            input()
            subprocess.call('clear' if os.name == 'posix' else 'cls')

        print('Full: ')
        for transition in transitions_:
            for row in transition:
                print(" ".join(map(str, row)))

            print('_________')

    def find_blank(matrix):
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    return i, j

    def get_moving_edge_values(matrix):
        pieces = []
        x1, y1 = find_blank(matrix)
        for move in moves:
            x = move[0] + x1
            y = move[1] + y1
            if 0 <= x < 3 and 0 <= y < 3:
                pieces.append([(x, y), (x1, y1)])

        return pieces

    def solve():
        global itr
        itr = 0

        for depth in range(max_depth):
            visited = set()
            print(depth)
            if dfs(pz, depth, visited):
                print(depth)
                transitions.append(pz.get_initial_state())
                print(iddfs_solution)
                iddfs_solution.append('Finished')
                display_puzzle_transitions(list(reversed(transitions)))

                return True
        print(f'Can\'t find solution in depth {max_depth} for {pz.get_initial_state()}')
        return False

    def dfs(puzzle_, depth, visited):
        global itr
        itr += 1
        if puzzle_.check_solved():
            return True

        if depth == 0:

            return False

        adj_list = get_moving_edge_values(puzzle_.get_matrix())

        while adj_list:
            pieces = adj_list.pop()
            new_puzzle = Puzzle([list(row) for row in puzzle_.get_matrix()])
            new_puzzle.move(pieces)
            new_puzzle.set_last_move(pieces)
            new_state = tuple(map(tuple, new_puzzle.get_matrix()))
            new_visited = visited.copy()

            if new_state not in visited:

                new_visited.add(new_state)

                if dfs(new_puzzle, depth - 1, new_visited):
                    transitions.append(new_puzzle.get_matrix())

                    return True
        return False

    solve()
    global itr
    print('iterations=', itr)
