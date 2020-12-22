# 824. Goat Latin
# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:      
        
        res = ""
        for i, word in enumerate(S.split()):
            if word[0] not in "AEIOUaeiou":
                res += word[1:] + word[0] + "ma" + "a"*(i+1) + " "
            else:
                res += word + "ma" + "a" *(i+1) + " "
                    
        return res.strip()
    



# Using Array
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels="AEIOUaeiou"
        res = []
        for i, word in enumerate(S.split()):
            if word[0] not in vowels:
                s_helper = word[:1]
                word = word[1:] + s_helper + "ma"
            else:
                word = word + "ma"
            
            res.append( word + "a" * (i+1) )
        
        return ' '.join(res)
    