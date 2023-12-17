import sys

filename = sys.argv[1]
sum = 0

with open(filename, "r") as file:
    line = file.readline().strip()
    line = line.split(",")

    for item in line:
        current = 0
        for char in item:
            ascii = ord(char)
            current += ascii
            current *= 17
            current %= 256
        sum += current

print(sum)
