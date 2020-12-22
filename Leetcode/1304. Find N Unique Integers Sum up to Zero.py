# 1304. Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = []
        
        a.extend([x for x in range(1, n // 2 + 1)])
        a.extend([-x for x in range(1, n // 2 + 1)])
        
        if len(a) != n:
            a.append(0)
            
        return a