nums = [2,7,11,15]
temp_nums = []
target = 9

for num in nums:
    print num
    temp_nums = nums
    
    index = nums.index(num) 
    print index
    del temp_nums[index]
    print nums
    print temp_nums
    