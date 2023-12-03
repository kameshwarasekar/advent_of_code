struct = []

with open("input.txt", "r") as file:
    sum = 0
    for index, line in enumerate(file):
        struct.append([])
        struct[index].append(".")
        line = line.strip()
        for char in line:
            struct[index].append(char)
        struct[index].append(".")
    struct.insert(0, ["."] * len(struct[0]))
    struct.append(struct[0])

    i = 1
    while i < len(struct) - 1:
        j = 1
        while j < len(struct[0]) - 1:
            number = ""
            add_to_sum = False
            num_start = -1
            if struct[i][j].isdigit():
                number += struct[i][j]
                num_start = j
                while struct[i][j + 1].isdigit():
                    number += struct[i][j + 1]
                    j += 1
                if number != "":
                    for k in range(num_start - 1, j + 2):
                        if struct[i - 1][k] != "." and not struct[i - 1][k].isdigit():
                            add_to_sum = True
                            break
                        if struct[i + 1][k] != "." and not struct[i + 1][k].isdigit():
                            add_to_sum = True
                            break
                    for k in range(i - 1, i + 2):
                        if (
                            struct[k][num_start - 1] != "."
                            and not struct[k][num_start - 1].isdigit()
                        ):
                            add_to_sum = True
                            break
                        if struct[k][j + 1] != "." and not struct[k][j + 1].isdigit():
                            add_to_sum = True
                            break
                    if add_to_sum:
                        sum += int(number)
            j += 1
        i += 1
    print(sum)
