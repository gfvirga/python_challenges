# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = 0
        res = []
        capacity = s.count(')')
        
        for char in s:
            if char == "(":
                if opened == capacity : continue
                opened += 1
            elif char == ")":
                capacity -= 1
                if not opened: continue
                opened -= 1
            res.append(char)
        
                
        return ''.join(res)
        
