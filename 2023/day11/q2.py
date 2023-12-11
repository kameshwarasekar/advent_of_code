import sys

filename = sys.argv[1]
h_index = []
length = -1


def new_index(pos, factor, h_index, v_indexes):
    x_count = 0
    y_count = 0
    while x_count < len(h_index) and pos[0] > h_index[x_count]:
        x_count += 1
    while y_count < len(v_indexes) and pos[1] > v_indexes[y_count]:
        y_count += 1
    return (pos[0] + x_count * (factor - 1), pos[1] + y_count * (factor - 1))


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
                galaxy_index.append((index, g_index))
                if g_index in v_indexes:
                    v_indexes.remove(g_index)

# count = 0
# # could have just reversed without count :facepalm
# for index in v_indexes:
#     for i in range(len(matrix)):
#         matrix.append(matrix[0][: index + count] + "." + matrix[0][index + count :])
#         matrix.pop(0)
#     count += 1
# for index in h_index[::-1]:
#     matrix.insert(index, "." * len(matrix[0]))

# print(matrix)

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == "#":
#             galaxy_index.append((i, j))
factor = 1000000
v_indexes = sorted(list(v_indexes))
new_galaxy_index = []
print(v_indexes)
for galaxy in galaxy_index:
    new_galaxy_index.append(new_index(galaxy, factor, h_index, v_indexes))

print(galaxy_index)
print(new_galaxy_index)
sum = 0
for i in range(len(new_galaxy_index)):
    for k in range(i + 1, len(new_galaxy_index)):
        sum += abs(new_galaxy_index[i][1] - new_galaxy_index[k][1]) + abs(
            new_galaxy_index[i][0] - new_galaxy_index[k][0]
        )
print(sum)
print("hello")


# def new_index(pos, factor):
#     x_count = 0
#     y_count = 0
#     while pos[0] > h_index[x_count]:
#         x_count += 1
#     while pos[1] > v_indexes[y_count]:
#         y_count += 1
#     return (pos[0] + x_count * factor, pos[1] + y_count * factor)
