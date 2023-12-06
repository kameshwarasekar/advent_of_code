import sys

count = 1
file_name = sys.argv[1]
with open(file_name) as file:
    line = file.readline().strip().split(" ")
    time = [x for x in line if x.isdigit()]
    line = file.readline().strip().split(" ")
    distance = [x for x in line if x.isdigit()]

print(time, distance)


for t, d in zip(time, distance):
    sub_count = 0
    for sec in range(int(t)):
        if sec == 0:
            dist = 0
        dist = (int(t) - sec) * sec
        if dist > int(d):
            sub_count += 1
    if sub_count > 0:
        count *= sub_count

print(count)
