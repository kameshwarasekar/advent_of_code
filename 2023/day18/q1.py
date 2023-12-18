import sys
import collections


filename = sys.argv[1]
blocks = collections.defaultdict(list)
current = (0, 0)
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        info = line.split(" ")
        if info[1] == "R":
            for i in range(current[1] + 1, current[1] + int(info[0]) + 1):
                blocks[current[0]].append(i)
            current = (current[0], current[1] + int(info[0]))
        if info[1] == "U":
            for i in range(current[0] - 1, current[0] - int(info[0]) - 1, -1):
                blocks[i].append(current[1])
            current = (current[0] - int(info[0]), current[1])
        if info[1] == "D":
            for i in range(current[0] + 1, current[0] + int(info[0]) + 1):
                blocks[i].append(current[1])
            current = (current[0] + int(info[0]), current[1])
        if info[1] == "L":
            for i in range(current[1] - 1, current[1] - int(info[0]) - 1, -1):
                blocks[current[1]].append(i)
            current = (current[0], current[1] - int(info[0]))
