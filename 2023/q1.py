import sys
from functools import cmp_to_key

filename = sys.argv[1]
hands = []
priority = {}
value = 0

for num in range(2, 10):
    priority[str(num)] = value
    value += 1

for ch in ["T", "J", "Q", "K", "A"]:
    priority[ch] = value
    value += 1

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        item = line.split(" ")
        hands.append((item[0], int(item[1])))

total_hands = len(hands)
print(total_hands)


def camel_cards_sort(pair1, pair2):
    hand1 = pair1[0]
    hand2 = pair2[0]

    set1 = set(hand1)
    set2 = set(hand2)
    if len(set1) < len(set2):
        return -1
    elif len(set1) > len(set2):
        return 1
    else:
        if len(set1) == 2:
            count1 = max(hand1.count(list(set1)[0]), hand1.count(list(set1)[1]))
            count2 = max(hand2.count(list(set2)[0]), hand2.count(list(set2)[1]))
            if count1 > count2:
                return -1
            elif count1 < count2:
                return 1
        if len(set1) == 3:
            # print("here")
            count1 = max(
                hand1.count(list(set1)[0]),
                hand1.count(list(set1)[1]),
                hand1.count(list(set1)[2]),
            )
            count2 = max(
                hand2.count(list(set2)[0]),
                hand2.count(list(set2)[1]),
                hand2.count(list(set2)[2]),
            )
            # print(count1, count2)
            if count1 > count2:
                return -1
            elif count1 < count2:
                return 1
        for i, j in zip(hand1, hand2):
            if i != j:
                return -1 if priority[i] > priority[j] else 1


hands.sort(key=cmp_to_key(camel_cards_sort))
hands_len = len(hands)
sum = 0
for hand, bet in hands:
    sum += bet * hands_len
    hands_len -= 1
print(sum)
