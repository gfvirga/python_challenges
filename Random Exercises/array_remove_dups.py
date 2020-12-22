def remove_dups(nums):
    pointer = 0
    while pointer < len(nums):
        # look back to see if previous number is duplicate
        if nums[pointer] == nums[pointer-1]:
            nums.pop(pointer) # remove element
        else:
            pointer += 1 # increment forward
    print nums      
array = [0,0,1,1,1,2,2,3,3,4,4,4,4]
remove_dups(array)