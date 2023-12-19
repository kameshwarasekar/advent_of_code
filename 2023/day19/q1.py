import sys
import collections


filename = sys.argv[1]
instructions = collections.defaultdict(list)
inputs = []
accepted = []
xmas_indexes = {"x": 0, "m": 1, "a": 2, "s": 3}


def processing(item):
    stack = []
    for criteria in instructions["in"]:
        if ">" in criteria[0]:
            check = criteria.split(">")
            if item[xmas_indexes[check[0]]] > int(check[1]):
                stack.append()


with open(filename, "r") as file:
    line = file.readline().strip()
    while len(line.strip()) != 0:
        parts = line[:-1].split("{")
        conditions = parts[1].split(",")
        for condition in conditions:
            criteria = condition.split(":")
            instructions[parts[0]].append(criteria)
        line = file.readline().strip()
    # print(instructions)
    line = file.readline().strip()
    while line:
        values = line[1:-1].split(",")
        input_row = []
        for value in values:
            input_row.append(int(value.split("=")[-1]))
        inputs.append(input_row)
        line = file.readline().strip()

for input in inputs:
    processing(input)
print(input)
