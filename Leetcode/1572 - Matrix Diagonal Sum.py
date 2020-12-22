#1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = 0
        col = 0
        scol = len(mat[0])-1
        counter = 0
        while row < len(mat) and col < len(mat[0]):
            if scol == col:
                counter += mat[row][col]
            else:
                counter += mat[row][col] + mat[row][scol]
            row = col = row + 1
            scol -= 1
            
        return counter