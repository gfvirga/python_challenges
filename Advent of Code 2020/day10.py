file = open('day10input.txt',mode='r')
nums = [int(line) for line in file.read().split("\n")]

diff = {
    1: 0,
    3: 0
}

nums.append(max(nums) + 3)

# Part One
i = 1
jolts_helper = 0
while i <= max(nums):
    jolts_helper += 1
    if i in nums:
        diff[jolts_helper] += 1
        jolts_helper = 0
    i += 1

print(f"Part One: {diff[1] * diff[3]}")


# Part Two
#¯\_(ツ)_/¯