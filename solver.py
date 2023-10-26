import copy
import os
import subprocess

from puzzle import Puzzle
from queue import PriorityQueue


def get_hamming_distance(puzzle):
    return sum((puzzle.get_matrix_as_list().index(node) == puzzle.get_initial_matrix_as_list().index(node))
               for node in range(0, 9))


itr = 0

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_blank(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return i, j


def get_moving_edge_values(matrix: [[]]):
    pieces = []
    x1, y1 = find_blank(matrix)
    for move in moves:
        x = move[0] + x1
        y = move[1] + y1
        if 0 <= x < 3 and 0 <= y < 3:
            pieces.append([(x, y), (x1, y1)])

    return pieces


def iddfs(pz: Puzzle, max_depth: int = 40):
    if not pz.is_solvable():
        print('Puzzle not solvable')
        return
    iddfs_solution = []
    transitions = []

    def display_puzzle_transitions(transitions_):

        # for i, state in enumerate(transitions_):
        #     for row in state:
        #         print(" ".join(map(str, row)))
        #     input()

        print('Full: ')
        for transition in transitions_:
            for row in transition:
                print(" ".join(map(str, row)))

            print('_________')

    def solve():
        global itr
        itr = 0

        for depth in range(max_depth):
            visited = set()
            print('depth=', depth)
            if dfs(pz, depth, visited):
                transitions.append(pz.get_initial_state())
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


#
# def shit(pz: Puzzle):
#     visited = set()
#     walk = []
#     moves_dict = {}
#
#     walk.append([pz, pz.heuristic()])
#
#     moves_dict[pz] = (None, None)
#
#     while walk:
#
#         current_puzzle, _  = sorted(walk, key=lambda x: x[1]).pop()
#
#         print(_)
#
#         for line in current_puzzle.get_matrix():
#             print(line)
#         print('==================')
#         input()
#
#         if current_puzzle.check_solved():
#             solution_path = []
#             while current_puzzle:
#                 previous_puzzle, last_move = moves_dict[current_puzzle]
#                 if last_move:
#                     solution_path.append(current_puzzle.get_matrix())
#                 current_puzzle = previous_puzzle
#             return list(reversed(solution_path))
#
#         visited.add(tuple(map(tuple, current_puzzle.get_matrix())))
#         adj_list = get_moving_edge_values(current_puzzle.get_matrix())
#         for move in adj_list:
#             new_puzzle = Puzzle([list(row) for row in current_puzzle.get_matrix()])
#             new_puzzle.move(move)
#
#             if tuple(map(tuple, new_puzzle.get_matrix())) not in visited:
#                 walk.append([new_puzzle, new_puzzle.misplaced_tiles()])
#                 moves_dict[new_puzzle] = (current_puzzle, move)
#
#     return []


def greedy(puzzle):
    opened = []
    closed = []

    opened.append(puzzle)
    iterations = 0

    def get_new_nodes(puzzle_):
        edges = get_moving_edge_values(puzzle_.get_matrix())
        new_nodes_ = []
        for edge in edges:
            x1, y1 = edge[0]
            x2, y2 = edge[1]
            new_matrix = [list(row) for row in puzzle_.get_matrix()]  # Create a new copy of the matrix
            new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
            new_puzzle_ = Puzzle(new_matrix, depth=puzzle_.depth + 1, so_far_cost=puzzle.heuristic())
            new_nodes_.append(new_puzzle_)
        return new_nodes_

    solution = {}

    while opened:
        opened = sorted(opened, key=lambda x: x.heuristic())
        iterations += 1
        node = opened.pop(0)
        solution[node.depth] = node.get_matrix()
        if node.check_solved():

            print("Puzzle solved!")
            for s in solution:
                print(s)
                for line in solution[s]:
                    print(line)
                print("===================")
            return True

        nodes = get_new_nodes(node)
        closed.append(node.matrix_as_tuple())

        for node_ in nodes:
            if node_.matrix_as_tuple() not in closed:
                opened.append(node_)
    return False
