number_strings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
d = dict(zip(number_strings, numbers))
with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        first_digit = -1
        last_digit = -1
        start_buffer = ""
        end_buffer = ""
        start = 0
        end = len(line) - 1

        while first_digit == -1 or last_digit == -1:
            if line[start].isdigit() and first_digit == -1:
                first_digit = line[start]
            if first_digit == -1:
                start_buffer = start_buffer + line[start]
                for num in number_strings:
                    if num in start_buffer[-6:]:
                        first_digit = d[num]
            if line[end].isdigit() and last_digit == -1:
                last_digit = line[end]
            if last_digit == -1:
                end_buffer = line[end] + end_buffer
                for num in number_strings:
                    if num in end_buffer[:6]:
                        last_digit = d[num]

            if last_digit == -1:
                end -= 1
            if first_digit == -1:
                start += 1
        sum += int(first_digit + last_digit)
    print(sum)
