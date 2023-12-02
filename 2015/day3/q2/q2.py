import collections

houses = set()

with open("input.txt", "r") as file:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    houses.add((x1, y1))
    for line in file:
        line = line.strip()
        for index, item in enumerate(line):
            if index % 2 == 0:
                if item == "^":
                    y1 += 1
                elif item == "<":
                    x1 -= 1
                elif item == ">":
                    x1 += 1
                else:
                    y1 -= 1
                houses.add((x1, y1))
            else:
                if item == "^":
                    y2 += 1
                elif item == "<":
                    x2 -= 1
                elif item == ">":
                    x2 += 1
                else:
                    y2 -= 1
                houses.add((x2, y2))
    print(len(houses))
