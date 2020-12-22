# PLAGERISM ALERT
# I DID NOT SOLVE THIS ALONE. I COULDN'T UNDERSTAND. I've memorized the solution and everytime I try something I endup with the same.

# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_i = {}
        for i,c in enumerate(order):
            order_i[c] = i
        
        for i in range(len(words) -1):
            w1 = words[i]        
            w2 = words[i+1]
            
            for k in range(min(len(w1), len(w2))):

                if w1[k] != w2[k]:
                    if order_i[w1[k]] > order_i[w2[k]]:
                        return False
                    break
                else:
                    if len(w1) > len(w2):
                        return False
                        
        return True
        
