from os import eventfd_read, stat_result


with open("input1.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        first_digit = -1
        last_digit = -1
        start = 0
        end = len(line) - 1
        while first_digit == -1 or last_digit == -1:
            if line[start].isdigit() and first_digit == -1:
                first_digit = line[start]
            if line[end].isdigit() and last_digit == -1:
                last_digit = line[end]
            if first_digit == -1:
                start += 1
            if last_digit == -1:
                end -= 1

        sum += int(line[start] + line[end])

    print(sum)
