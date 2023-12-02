max_quantity = {"red": 12, "blue": 14, "green": 13}

with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        flag = True
        line = line.strip()
        line = line[5:]
        parts = line.split(": ")
        game_id = int(parts[0])
        sets = parts[1].split("; ")
        for set in sets:
            if flag == True:
                balls_comb = set.split(", ")
                for balls in balls_comb:
                    if flag == True:
                        value = balls.split(" ")
                        if max_quantity[value[1]] < int(value[0]):
                            flag = False
        if flag == True:
            sum += game_id
    print(sum)
