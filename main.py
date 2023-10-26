from pprint import pprint
import time

from puzzle import Puzzle
from solver import iddfs, greedy

if __name__ == '__main__':

    puzzle = Puzzle([[8, 6, 7], [2, 5, 4], [0, 3, 1]])
    #
    # iddfs(puzzle, max_depth=31)

    # puzzle = Puzzle([[2, 5, 3], [1, 0, 6], [4, 7, 8]])
    #
    # iddfs(puzzle, max_depth=31)

    # puzzle = Puzzle([[2, 7, 5], [0, 8, 4], [3, 1, 6]])
    #
    # iddfs(puzzle, max_depth=31)

    # Invalid input
    # puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [8, 7, 0]])

    # iddfs(puzzle, max_depth=31)
    # pprint(greedy(puzzle, 'hamming_distance'))
    # pprint(greedy(puzzle, 'manhattan_distance'))
    # pprint(greedy(puzzle, 'hamming_distance'))

    start_time = time.time()
    iddfs_result, iddfs_calls = iddfs(puzzle, max_depth=31)
    iddfs_time = time.time() - start_time

    heuristic_functions = ['hamming_distance', 'manhattan_distance', 'linear_conflict']

    results = {}
    call_counts = {}
    execution_times = {}

    for heuristic_function in heuristic_functions:
        start_time = time.time()
        result, calls = greedy(puzzle, heuristic_function)
        execution_time = time.time() - start_time

        results[heuristic_function] = result
        call_counts[heuristic_function] = calls
        execution_times[heuristic_function] = execution_time

    fastest_heuristic = min(execution_times, key=lambda k: execution_times[k])

    print(f"IDDFS Solution:\n{iddfs_result}")
    print(f"IDDFS Function Calls: {iddfs_calls}")
    print(f"IDDFS Execution Time: {iddfs_time} seconds\n")

    for heuristic_function in heuristic_functions:
        print(f"{heuristic_function} Solution:\n{results[heuristic_function]}")
        print(f"{heuristic_function} Function Calls: {call_counts[heuristic_function]}")
        print(f"{heuristic_function} Execution Time: {execution_times[heuristic_function]} seconds\n")

    print(f"Fastest Heuristic: {fastest_heuristic}")
    print(results)
