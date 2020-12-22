# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = list(zip(indices,s))
        a.sort()
        res = ""
        for i, l in a:
            res += l
        return res