with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        counter = 0
        for index, item in enumerate(line):
            counter = counter + 1 if item == "(" else counter - 1
            if counter == -1:
                print(index + 1)
                break

        print(counter)
