import re


class Puzzle:
    def __init__(self, matrix: [[]]):
        self.__last_move = None
        self.__matrix = matrix
        self.__initial_state = matrix
        self.adj_list = None
        self.positions = [[] for _ in range(9)]

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

    def check_solved(self):
        if self.__matrix in [
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
        ]:
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
