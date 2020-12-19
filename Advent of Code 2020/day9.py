
file = open('./inputs/day9input.txt',mode='r')
nums = [int(line) for line in file.read().split("\n")]

#Two Sum
def two_sum(num, array):
    left = 0
    right = len(array)-1
    while left < right:
        sum = array[right] + array[left] 
        if sum == num:
            return True
        if sum > num:
            right -= 1
        else:
            left += 1
    return False

# Part one
preamble = 24
for i in range(preamble,len(nums)):
    num = nums[i+1]
    array = sorted(nums[i-preamble:i+1])
    if not two_sum(num,array):       
        break
print(f"Part One: {num}")

# Part Two
left = 0
right = len(nums)-1
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if sum(nums[i:j]) == num:
            if i == j-1 : continue
            print(f"Part Two: {min(nums[i:j]) + max(nums[i:j])}")