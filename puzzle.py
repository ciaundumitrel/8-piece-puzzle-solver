import re


class Puzzle:
    def __init__(self, matrix: [[]], depth=0, so_far_cost=0):
        self.__last_move = None
        self.__matrix = matrix
        self.__initial_state = matrix
        self.adj_list = None
        self.positions = [[] for _ in range(9)]
        self.depth = depth
        self.so_far_cost = so_far_cost

    def matrix_as_tuple(self):
        return tuple(map(tuple, self.__matrix))

    def count_inversions(self):
        inversions = 0
        puzzle = [number for row in self.__matrix for number in row if number != 0]
        for i in range(len(puzzle)):
            for j in range(i + 1, len(puzzle)):
                if puzzle[i] > puzzle[j]:
                    inversions += 1
        return inversions

    def is_solvable(self):
        inversions = self.count_inversions()
        if inversions % 2 == 0:
            return True
        else:
            blank_row = 0
            for i in range(3):
                if 0 in self.__matrix[i]:
                    blank_row = 3 - i
                    break
            return (inversions + blank_row) % 2 == 1

    def get_matrix(self):
        return self.__matrix

    def set_last_move(self, move):
        self.__last_move = move

    def get_initial_state(self):
        return self.__initial_state

    def get_last_move(self):
        return self.__last_move

    def __str__(self):
        patterns = [r'\], \[', r'\[\[', r'\]\]']
        cleaned_matrix = str(self.__matrix)
        for pattern in patterns:
            cleaned_matrix = re.sub(pattern, '\n', cleaned_matrix)
        cleaned_matrix = cleaned_matrix.replace(',', '').replace('\'', '')
        return cleaned_matrix

    @staticmethod
    def get_goal_states():
        return [
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
            [[1, 0, 2],
             [3, 4, 5],
             [6, 7, 8]],
            [[1, 2, 0],
             [3, 4, 5],
             [6, 7, 8]],
            [[1, 2, 3],
             [0, 4, 5],
             [6, 7, 8]],
            [[1, 2, 3],
             [4, 0, 5],
             [6, 7, 8]],
            [[1, 2, 3],
             [4, 5, 0],
             [6, 7, 8]],
            [[1, 2, 3],
             [4, 5, 6],
             [0, 7, 8]],
            [[1, 2, 3],
             [4, 5, 6],
             [7, 0, 8]],
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]],
        ]

    def check_solved(self):
        if self.__matrix in Puzzle.get_goal_states():
            return True
        return False

    def get_position(self, piece):
        for line in self.__matrix:
            for item in line:
                if piece == item:
                    return self.__matrix.index(line), line.index(piece)

    def move(self, move):
        x1, y1 = move[0]
        x2, y2 = move[1]

        self.__matrix[x1][y1], self.__matrix[x2][y2] = self.__matrix[x2][y2], self.__matrix[x1][y1]

        return True

    def move_back(self):
        self.move(self.__last_move)

    def heuristic(self):

        # return misplaced_tiles(self.__matrix) + manhattan_distance(self.__matrix)
        # return hamming_distance(self.__matrix)
        # print(self.manhattan_distance())
        # return self.manhattan_distance() + self.misplaced_tiles()
        # return self.misplaced_tiles()
        print(self.depth)
        return self.misplaced_tiles()
    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def manhattan_distance(self):
        state1 = self.__matrix
        n = 3
        min_distance = 999

        for state2 in self.get_goal_states():
            distance = 0
            for i in range(n):
                for j in range(n):
                    tile = state1[i][j]
                    if tile != 0:
                        row1, col1 = divmod(tile - 1, n)  # Calculate the target position for the tile in state1
                        for x in range(n):
                            for y in range(n):
                                if state2[x][y] == tile:
                                    row2, col2 = x, y  # Find the corresponding position of the tile in state2
                                    distance += abs(row1 - row2) + abs(col1 - col2)

            min_distance = min(min_distance, distance)

        return min_distance

    def misplaced_tiles(self):

        goals = Puzzle.get_goal_states()

        min_count = 10
        # The goal state
        for goal in goals:
            count = 0
            for i in range(3):
                for j in range(3):
                    if self.__matrix[i][j] != goal[i][j]:
                        count += 1
            if min_count > count:
                min_count = count
        return min_count


