# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        rev = list(reversed([e for e in S if e.isalpha()]))
        res = ""
        for i in S:
            if i.isalpha():
                res += rev[0]
                rev.pop(0)
            else:
                res += i
        return res