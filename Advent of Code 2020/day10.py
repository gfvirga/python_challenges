file = open('day10input.txt',mode='r')
nums = [int(line) for line in file.read().split("\n")]

diff = {
    1: 0,
    3: 0
}

nums.append(0)
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

def valid(array):
    i = 1
    jolts_helper = 0
    while i <= max(array):
        jolts_helper += 1
        if i in array: 
            jolts_helper = 0
        if jolts_helper > 3:
            return False
        i += 1
    return True

result = 0
counter = 0
nums.sort()
for i in range(1,len(nums)):
    print(nums[:i] + nums[i+1:])
    if valid(nums[:i] + nums[i+1:]):
        result += 1
        print(result)

print(result)