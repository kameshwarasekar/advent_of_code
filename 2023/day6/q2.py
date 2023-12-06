import sys

count = 0
time = ""
distance = ""
file_name = sys.argv[1]
with open(file_name) as file:
    line = file.readline().strip().split(" ")
    for x in line:
        if x.isdigit():
            time += x
    line = file.readline().strip().split(" ")
    for x in line:
        if x.isdigit():
            distance += x

print(time, distance)


for sec in range(int(time)):
    if sec == 0:
        dist = 0
    dist = (int(time) - sec) * sec
    if dist > int(distance):
        print(
            (int(time) - sec) - sec + 1
        )  # solving a lot of computation based on the question.
        # If not I need to loop through the entrie range and
        # increment count on success (time consuming)
        break

print(count)
