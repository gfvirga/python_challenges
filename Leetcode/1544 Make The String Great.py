# 1544. Make The String Great
# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s)-1:
            if s[i].upper() == s[i+1].upper():
                if (s[i+1].isupper() and s[i].islower()) or (s[i+1].islower() and s[i].isupper()):
                    s = s[:i] + s[i+2:]
                    i = 0
                else:
                    i += 1
            else:
                i += 1
        return s
        