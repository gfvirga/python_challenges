# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = 0
        res = []
        for n in nums:
            rsum += n
            res.append(rsum)
            
        return res