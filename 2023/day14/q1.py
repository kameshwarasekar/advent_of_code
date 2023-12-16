import sys
import collections

filename = sys.argv[1]
cols = 0
with open(filename, "r") as file:
    line = file.readline()
    cols = len(line.strip())

limits = [0] * cols
round_balls = collections.OrderedDict()
size = 0
index = 0
with open(filename, "r") as file:
    for line in file:
        round_balls[index] = 0
        for pos, char in enumerate(line.strip()):
            if char == "O":
                round_balls[limits[pos]] += 1
                limits[pos] += 1
            if char == "#":
                limits[pos] = index + 1
        size += 1
        index += 1
sum = 0
for row in round_balls.values():
    sum += size * row
    size -= 1

print(sum)
