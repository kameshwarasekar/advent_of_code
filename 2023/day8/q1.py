import sys

count = 0
filename = sys.argv[1]
paths = {}
instructions = ""
current = "AAA"
with open(filename, "r") as file:
    instructions = file.readline().strip()
    line = file.readline()
    while line:
        line = line.strip()
        if len(line) > 0:
            nodes = line.split(" ")
            print(nodes)
            paths[nodes[0]] = (nodes[2][1:-1], nodes[3][:-1])
        line = file.readline()

    while 1:
        current = (
            paths[current][0]
            if instructions[count % len(instructions)] == "L"
            else paths[current][1]
        )
        count += 1
        if current == "ZZZ":
            print(count)
            break
