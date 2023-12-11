import sys

filename = sys.argv[1]
s_pos = (-1, -1)
# dict {(x,y) = symbol}
nodes = {}
maxi = 0
visited = set()


def bfs():
    global maxi
    queue = []
    visited.add(s_pos)
    del nodes[s_pos]
    if nodes.get((s_pos[0] + 1, s_pos[1]), None) in ["L", "J", "|"]:
        queue.append(((s_pos[0] + 1, s_pos[1]), 1, nodes[(s_pos[0] + 1, s_pos[1])]))
        visited.add((s_pos[0] + 1, s_pos[1]))
    if nodes.get((s_pos[0] - 1, s_pos[1]), None) in ["F", "7", "|"]:
        queue.append(((s_pos[0] - 1, s_pos[1]), 1, nodes[(s_pos[0] - 1, s_pos[1])]))
        visited.add((s_pos[0] - 1, s_pos[1]))
    if nodes.get((s_pos[0], s_pos[1] + 1), None) in ["-", "J", "7"]:
        queue.append(((s_pos[0], s_pos[1] + 1), 1, nodes[(s_pos[0], s_pos[1] + 1)]))
        visited.add((s_pos[0], s_pos[1] + 1))
    if nodes.get((s_pos[0], s_pos[1] - 1), None) in ["-", "L", "F"]:
        queue.append(((s_pos[0], s_pos[1] - 1), 1, nodes[(s_pos[0], s_pos[1] - 1)]))
        visited.add((s_pos[0], s_pos[1] - 1))

    print(queue)
    while len(queue) > 0:
        (x, y), dist, symbol = queue.pop(0)
        next = 0
        if dist > maxi:
            maxi = dist
        if symbol == "|":
            next = (x + 1, y) if (x + 1, y) not in visited else (x - 1, y)
        if symbol == "-":
            next = (x, y - 1) if (x, y - 1) not in visited else (x, y + 1)
        if symbol == "J":
            next = (x - 1, y) if (x - 1, y) not in visited else (x, y - 1)
        if symbol == "L":
            next = (x - 1, y) if (x - 1, y) not in visited else (x, y + 1)
        if symbol == "F":
            next = (x, y + 1) if (x, y + 1) not in visited else (x + 1, y)
        if symbol == "7":
            next = (x, y - 1) if (x, y - 1) not in visited else (x + 1, y)
        if next == s_pos:
            return
        if next not in visited and nodes.get(next, None) is not None:
            queue.append((next, dist + 1, nodes[next]))
            visited.add(next)


with open(filename, "r") as file:
    for row, line in enumerate(file):
        symbols = line.strip()
        for col, symbol in enumerate(symbols):
            if symbol != ".":
                nodes[(row, col)] = symbol
            if symbol == "S":
                s_pos = (row, col)


print(nodes)
print(s_pos)

bfs()
print(maxi)
