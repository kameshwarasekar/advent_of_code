import sys

filename = sys.argv[1]
sum = 0
flag = False
beginning_sum = 0


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
        l = []
        nums = line.split(" ")
        nums = [int(x) for x in nums]
        beginning_sum = nums[0]
        while not flag:
            # print(nums)
            l.append(nums[0])
            nums = prediction(nums)
            if nums is not None:
                # print(beginning_sum, nums)
                beginning_sum -= nums[0] if beginning_sum >= 0 else -nums[0]
        flag = False
        # print(beginning_sum)
        temp_sum = 0
        # l.append(0)
        print(l)
        for i in range(len(l) - 1, -1, -1):
            temp_sum = l[i] - temp_sum
            print(temp_sum)
        print("temp_sum", temp_sum)
        sum += temp_sum
    print(sum)
