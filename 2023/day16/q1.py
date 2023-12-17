import sys
import collections

filename = sys.argv[1]
visited = collections.defaultdict(list)
matrix = []

with open(filename, "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

stack = []
stack.append((0, 0, "r"))
directions = {"r": (0, 1), "d": (1, 0), "l": (0, -1), "u": (-1, 0)}
# direction = 'r'
print(matrix)
while stack:
    x, y, direction = stack.pop()
    if (
        x >= 0
        and y >= 0
        and x < len(matrix)
        and y < len(matrix[0])
        and direction not in visited[(x, y)]
    ):
        visited[(x, y)].append(direction)
        char = matrix[x][y]
        if char == ".":
            stack.append(
                (x + directions[direction][0], y + directions[direction][1], direction)
            )
        elif char == "/":
            direction = (
                "u"
                if direction == "r"
                else "r"
                if direction == "u"
                else "d"
                if direction == "l"
                else "l"
            )
            stack.append(
                (x + directions[direction][0], y + directions[direction][1], direction)
            )
        elif char == "\\":
            # direction = "l" if direction == "u" else "u"
            print("here", (x, y, direction))
            direction = (
                "l"
                if direction == "u"
                else "u"
                if direction == "l"
                else "r"
                if direction == "d"
                else "d"
            )
            stack.append(
                (x + directions[direction][0], y + directions[direction][1], direction)
            )
        elif char == "|":
            if direction in ["u", "d"]:
                stack.append(
                    (
                        x + directions[direction][0],
                        y + directions[direction][1],
                        direction,
                    )
                )
            else:
                stack.append((x + directions["u"][0], y + directions["u"][1], "u"))
                stack.append((x + directions["d"][0], y + directions["d"][1], "d"))
        elif char == "-":
            if direction in ["r", "l"]:
                stack.append(
                    (
                        x + directions[direction][0],
                        y + directions[direction][1],
                        direction,
                    )
                )
            else:
                stack.append((x + directions["r"][0], y + directions["r"][1], "r"))
                stack.append((x + directions["l"][0], y + directions["l"][1], "l"))

print(len(visited))
