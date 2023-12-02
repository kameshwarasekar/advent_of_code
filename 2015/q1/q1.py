with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        counter = 0
        for item in line:
            counter = counter + 1 if item == "(" else counter - 1
        print(counter)
