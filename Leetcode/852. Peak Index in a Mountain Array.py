# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                return i
        
        return -1