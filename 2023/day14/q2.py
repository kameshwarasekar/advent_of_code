# import sys
# import collections

# filename = sys.argv[1]
# cols = 0
# with open(filename, "r") as file:
#     line = file.readline()
#     cols = len(line.strip())

# limits = [0] * cols
# round_balls = collections.OrderedDict()
# size = 0
# index = 0
# with open(filename, "r") as file:
#     for line in file:
#         round_balls[index] = 0
#         for pos, char in enumerate(line.strip()):
#             if char == "O":
#                 round_balls[limits[pos]] += 1
#                 limits[pos] += 1
#             if char == "#":
#                 limits[pos] = index + 1
#         size += 1
#         index += 1
# sum = 0
# for row in round_balls.values():
#     sum += size * row
#     size -= 1

# print(sum)


import sys
import collections

filename = sys.argv[1]
cols = 0
with open(filename, "r") as file:
    line = file.readline().strip()
    cols = len(line)

n_limits = [0] * cols
board = []  # this is the matrix
size = 0


def east_tilt(board):
    for row in range(len(board)):
        limit = len(board[row]) - 1
        for char in range(len(board[row]) - 1, -1, -1):
            if board[row][char] == "O":
                board[row][char] = "."
                board[row][limit] = "O"
                limit -= 1
            if board[row][char] == "#":
                limit = char - 1
    return board


def south_tilt(board):
    global cols
    s_limits = [len(board) - 1] * cols
    for i in range(len(board) - 1, -1, -1):
        for k in range(len(board[i])):
            if board[i][k] == "O":
                board[i][k] = "."
                board[s_limits[k]][k] = "O"
                s_limits[k] -= 1
            if board[i][k] == "#":
                s_limits[k] = i - 1
    board = east_tilt(board)
    return board


def west_tilt(board):
    for row in range(len(board)):
        limit = 0
        for char in range(len(board[row])):
            if board[row][char] == "O":
                board[row][char] = "."
                board[row][limit] = "O"
                limit += 1
            if board[row][char] == "#":
                limit = char + 1
    board = south_tilt(board)
    return board


def north_tilt(board):
    global cols
    n_limits = [0] * cols
    for i in range(len(board)):
        for k in range(len(board[0])):
            if board[i][k] == "O":
                board[i][k] = "."
                board[n_limits[k]][k] = "O"
                n_limits[k] += 1
            if board[i][k] == "#":
                n_limits[k] = i + 1
    board = west_tilt(board)
    return board


with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        board.append(list(line))

for i in range(1000000000):
    board = north_tilt(board)


sum = 0
index = 1
for line in board[::-1]:
    line = "".join(line)
    sum += line.count("O") * index
    index += 1
print(sum)

# for line in board:
#     print("".join(line))
