# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        decreasing = True
        increasing = True
        
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                decreasing = False
            elif A[i-1] > A[i]:
                increasing = False
                
        return decreasing or increasing