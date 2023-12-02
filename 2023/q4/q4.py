with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        line = line[5:]
        parts = line.split(": ")
        game_id = int(parts[0])
        sets = parts[1].split("; ")
        colors = {"red": 0, "blue": 0, "green": 0}
        sub_sum = 1
        for set in sets:
            balls_comb = set.split(", ")
            for balls in balls_comb:
                value = balls.split(" ")
                colors[value[1]] = max(colors[value[1]], int(value[0]))
        for color in colors.values():
            sub_sum *= color
        sum += sub_sum

    print(sum)
