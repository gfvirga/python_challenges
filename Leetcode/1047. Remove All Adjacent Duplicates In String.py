# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0

        S = list(S)
        while i < len(S) - 1:
            if S[i] == S[i+1]:
                del S[i]
                del S[i]
                i = 0 
            else:
                i += 1
                
        return S