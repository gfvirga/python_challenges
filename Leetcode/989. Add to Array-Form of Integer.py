# 989. Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
       
        return list(str(int(''.join(str(d) for d in A)) + K))