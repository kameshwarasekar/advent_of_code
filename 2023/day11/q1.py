import sys

filename = sys.argv[1]
h_index = []
length = -1
with open(filename, "r") as file:
    line = file.readline().strip()
    length = len(line)
v_indexes = set([x for x in range(length)])
matrix = []
galaxy_index = []

with open(filename, "r") as file:
    for index, line in enumerate(file):
        line = line.strip()
        matrix.append(line)
        unique = set(line)
        if len(unique) == 1 and "." in unique:
            h_index.append(index)
        for g_index, char in enumerate(line):
            if char == "#":
                if g_index in v_indexes:
                    v_indexes.remove(g_index)

count = 0
# could have just reversed without count :facepalm
for index in v_indexes:
    for i in range(len(matrix)):
        matrix.append(matrix[0][: index + count] + "." + matrix[0][index + count :])
        matrix.pop(0)
    count += 1
for index in h_index[::-1]:
    matrix.insert(index, "." * len(matrix[0]))

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "#":
            galaxy_index.append((i, j))

print(galaxy_index)
sum = 0
for i in range(len(galaxy_index)):
    for k in range(i + 1, len(galaxy_index)):
        sum += abs(galaxy_index[i][1] - galaxy_index[k][1]) + abs(
            galaxy_index[i][0] - galaxy_index[k][0]
        )
print(sum)
print("hello")
