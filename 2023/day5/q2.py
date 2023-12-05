import math


def perform_action(input):
    input_len = len(input)
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        while line:
            if not line:
                break
            if len(line) == 0:
                line = file.readline()
                line = line.strip()
                continue

            if len(line) > 0 and line[0].isalpha():
                line = file.readline().strip()
                new_sources = [-1] * input_len
                indexes_updated = 0

                while len(line) > 0 and line[0].isdigit():
                    d = line.split(" ")
                    for index, source in enumerate(input):
                        if (
                            indexes_updated != len(new_sources)
                            and new_sources[index] == -1
                        ):
                            if (
                                source >= int(d[1])
                                and source <= int(d[1]) + int(d[2]) - 1
                            ):
                                new_sources[index] = int(d[0]) + (source - int(d[1]))
                                indexes_updated += 1

                    line = file.readline().strip()
                for index, item in enumerate(new_sources):
                    if item == -1:
                        new_sources[index] = input[index]

                input = new_sources
            line = file.readline().strip()
        return min(input)


with open("input_1.txt", "r") as file:
    line = file.readline().strip()
    input_pairs = line[7:].split(" ")
    line = file.readline().strip()
    if len(line) > 0:
        input_pairs += line.split(" ")

    input = []
    min = math.inf

    for i in range(0, len(input_pairs), 2):
        input = []
        for j in range(int(input_pairs[i]), int(input_pairs[i + 1])):
            input.append(j)
        perform_action(input)

    # while line:
    #     if not line:
    #         break
    #     if len(line) == 0:
    #         line = file.readline()
    #         line = line.strip()
    #         continue

    #     if len(line) > 0 and line[0].isalpha():
    #         line = file.readline().strip()
    #         new_sources = [-1] * input_len
    #         indexes_updated = 0

    #         while len(line) > 0 and line[0].isdigit():
    #             d = line.split(" ")
    #             for index, source in enumerate(input):
    #                 if indexes_updated != len(new_sources) and new_sources[index] == -1:
    #                     if source >= int(d[1]) and source <= int(d[1]) + int(d[2]) - 1:
    #                         new_sources[index] = int(d[0]) + (source - int(d[1]))
    #                         indexes_updated += 1

    #             line = file.readline().strip()
    #         for index, item in enumerate(new_sources):
    #             if item == -1:
    #                 new_sources[index] = input[index]

    #         input = new_sources
    #     line = file.readline().strip()

    print(min(input))
