# with open("input.txt", "r") as file:
#     sum = 0
#     for line in file:
#         d = {}
#         matching = 0
#         line = line.strip()
#         parts = line.split(": ")
#         codes = parts[1].split(" | ")
#         for winning_num in codes[0].split(" "):
#             if winning_num.isdigit():
#                 d[winning_num] = 1
#         for num in codes[1].split(" "):
#             if num.isdigit():
#                 if d.get(num, None) != None:
#                     matching += 1
#         if matching > 0:
#             sum += 2 ** (matching - 1)
#     print(sum)
d = {}
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    last_line = lines[-1]
    card_num = last_line.split(": ")[0]
    original_cards_count = int(card_num[-(len(card_num) - 5) :])
    print("original_count: ", original_cards_count)
    for i in range(1, original_cards_count + 1):
        d[i] = 1

    for index, line in enumerate(lines):
        index = index + 1
        matching = 0
        d2 = {}
        line = line.strip()
        parts = line.split(": ")
        codes = parts[1].split(" | ")
        for winning_num in codes[0].split(" "):
            if winning_num.isdigit():
                d2[winning_num] = 1
        for num in codes[1].split(" "):
            if num.isdigit():
                if d2.get(num, None) != None:
                    matching += 1
        if matching > 0:
            for i in range(index + 1, index + 1 + matching):
                d[i] += d[index]
    sum = sum(d.values())
    print(sum)
