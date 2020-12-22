# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    
        for row in range(len(A)):
                A[row] =  [col ^ 1 for col in reversed(A[row])]     
        return A

# One line
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    
        return [[col ^ 1 for col in reversed(row)] for row in A]