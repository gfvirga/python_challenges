# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        for num in A:
             res.append(num * num)
        res.sort()
        return res