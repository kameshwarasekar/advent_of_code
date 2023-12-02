import collections

houses = set()

with open("input.txt", "r") as file:
    x = 0
    y = 0
    houses.add((x, y))
    for line in file:
        line = line.strip()
        for item in line:
            if item == "^":
                y += 1
            elif item == "<":
                x -= 1
            elif item == ">":
                x += 1
            else:
                y -= 1
            houses.add((x, y))
    print(len(houses))
