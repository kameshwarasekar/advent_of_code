import sys

filename = sys.argv[1]
sum = 0
flag = False
last_digit_sum = 0


def prediction(nums):
    diff = []
    zero_flag = True
    global flag
    # nums = line.split(" ")
    for i in range(1, len(nums)):
        difference = int(nums[i]) - int(nums[i - 1])
        diff.append(difference)
        if difference != 0 and zero_flag:
            zero_flag = False

    if not zero_flag:
        return diff
    else:
        flag = True
        return None


with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        # sum += prediction(line)
        nums = line.split(" ")
        nums = [int(x) for x in nums]
        while not flag:
            last_digit_sum += nums[-1]
            nums = prediction(nums)
        flag = False
    print(last_digit_sum)
