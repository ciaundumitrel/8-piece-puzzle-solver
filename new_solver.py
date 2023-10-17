def dfs(src, limit, visited_states):
    if check_final_state(src):
        return True
    if limit <= 0:
        return False

    visited_states.append(src)
    moves = possible_moves(src, visited_states)
    for move in moves:
        if dfs(move, limit - 1, visited_states):
            print(src)
            return True
    return False


def check_final_state(src):
    if src == [-1, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True


def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    if b not in [0, 1, 2]:
        d += 'u'
    if b not in [6, 7, 8]:
        d += 'd'
    if b not in [2, 5, 8]:
        d += 'r'
    if b not in [0, 3, 6]:
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state, move, b))
    return [move for move in pos_moves if move not in visited_states]


def gen(state, move, blank):
    temp = state.copy()
    if move == 'u':
        temp[blank - 3], temp[blank] = temp[blank], temp[blank - 3]
    if move == 'd':
        temp[blank + 3], temp[blank] = temp[blank], temp[blank + 3]
    if move == 'r':
        temp[blank + 1], temp[blank] = temp[blank], temp[blank + 1]
    if move == 'l':
        temp[blank - 1], temp[blank] = temp[blank], temp[blank - 1]
    return temp


def iddfs(src, depth):
    for i in range(depth):
        visited_states = []
        if dfs(src, i + 1, visited_states):
            print(src)
            return True
    return False


# Test 1
src = [1, 2, 3, -1, 4, 5, 6, 7, 8]

depth = 21
print(iddfs(src, depth))
