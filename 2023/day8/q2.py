import sys

count = 0
filename = sys.argv[1]
paths = {}
instructions = ""
current = []
with open(filename, "r") as file:
    instructions = file.readline().strip()
    line = file.readline()
    while line:
        line = line.strip()
        if len(line) > 0:
            nodes = line.split(" ")
            if nodes[0][-1] == "A":
                current.append(nodes[0])
            paths[nodes[0]] = (nodes[2][1:-1], nodes[3][:-1])
        line = file.readline()
    total = len(current)

    # print(instructions)
    # print(paths)
    print(total)
    print(current)
    while 1:
        z_count = 0
        for index, ghost in enumerate(current):
            # print(ghost)
            current[index] = (
                paths[ghost][0]
                if instructions[count % len(instructions)] == "L"
                else paths[ghost][1]
            )
            # print(ghost)
            if ghost[-1] == "Z":
                z_count += 1
        count += 1
        # print(current)
        # print(z_count)
        if z_count > 2:
            print(z_count, count, current)
        if z_count == total:
            print(count)
            break
