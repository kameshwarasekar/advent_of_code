with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        d = {}
        matching = 0
        line = line.strip()
        parts = line.split(": ")
        codes = parts[1].split(" | ")
        for winning_num in codes[0].split(" "):
            if winning_num.isdigit():
                d[winning_num] = 1
        for num in codes[1].split(" "):
            if num.isdigit():
                if d.get(num, None) != None:
                    matching += 1
        if matching > 0:
            sum += 2 ** (matching - 1)
    print(sum)
