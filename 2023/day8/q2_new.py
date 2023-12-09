import sys
import math

filename = sys.argv[1]
paths = {}
starts = []
node_counts = []


def perform(node):
    count = 0
    flag = False
    # print(node)
    while not flag:
        instruct = instructions[count % len(instructions)]
        node = paths[node][0] if instruct == "L" else paths[node][1]
        if node[-1] == "Z":
            flag = True
        count += 1
    node_counts.append(count)
    # print(node_counts)


with open(filename, "r") as file:
    instructions = file.readline().strip()
    line = file.readline().strip()
    line = file.readline().strip()
    while line:
        nodes = line.split(" ")
        paths[nodes[0]] = (nodes[2][1:-1], nodes[3][:-1])
        if nodes[0][-1] == "A":
            starts.append(nodes[0])
        line = file.readline().strip()
    # print(starts)
    for node in starts:
        perform(node)
    # print(node_counts)
    print(math.lcm(*node_counts))
