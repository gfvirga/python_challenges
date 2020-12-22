#1624. Largest Substring Between Two Equal Characters
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLength = -1
        
        for i, char in enumerate(s):
            if char in s[i:]:
                for j in range(i, len(s)):
                    if char == s[j]:
                        maxLength = max(j-1 - i, maxLength)
                        
        return maxLength