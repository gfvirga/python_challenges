# 1539 Kth Missing Positive Number.py
# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        i = 1
        while missing != k:
            if i not in arr:
                missing += 1
            i +=1
        return i-1
