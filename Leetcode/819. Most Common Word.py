# Plagerism Alert
# I came up with nmost of this solution, but the last line.
# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/



from collections import Counter 
import operator
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_clean = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
        words = Counter(paragraph_clean.split())
        
        for w in banned:
            if w in words:
                words.pop(w)
        
        return max(words.items(), key=operator.itemgetter(1))[0]