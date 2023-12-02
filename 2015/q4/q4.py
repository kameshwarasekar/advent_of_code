with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        l, w, h = tuple(line.split("x"))
        l, w, h = int(l), int(w), int(h)
        dimensions = sorted([l, w, h])
        sum += 2 * dimensions[0] + 2 * dimensions[1] + l * w * h
    print(sum)
