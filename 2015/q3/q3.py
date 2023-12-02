with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        l, w, h = tuple(line.split("x"))
        l, w, h = int(l), int(w), int(h)
        sum += min(l * w, w * h, h * l) + 2 * l * w + 2 * w * h + 2 * h * l
    print(sum)
