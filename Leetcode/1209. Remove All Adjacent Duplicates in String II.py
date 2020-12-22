# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        
        while i < len(s):
            checks = s[i]*k
            if checks in s:
                i = s.find(checks)
                s = s.replace(checks,'')
            else:
                i += 1
        
        return s