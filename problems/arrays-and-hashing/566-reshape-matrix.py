"""
Link: https://leetcode.com/problems/reshape-the-matrix
Difficulty: easy

Problem:
Reshape a 2d array if it can be transmutated

Input / Output:


Notes:


Solution Approaches:
Perform size check
Create new zero 2d array
Iterate and populate new matrix

"""
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(mat)*len(mat[0]): return mat
        res = [[0 for i in range(c)] for j in range(r)]
        n_c, n_r = 0,0 
        for row in mat:
            for num in row:
                res[n_r][n_c] = num
                n_c += 1
                if n_c == c:
                    n_c = 0
                    n_r+=1
        return res