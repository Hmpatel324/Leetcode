"""
Link: https://leetcode.com/problems/search-a-2d-matrix
Difficulty: medium

Problem:
given a m x n matrix
rows are non decreasing
head of each row is > tail of previous row
bool determine if a target exists

Input / Output:


Notes:


Solution Approaches:
2 x BST. BST 1 - find target row then BST 2 - find target column

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # BST - find row
        lo, hi = 0, len(matrix)-1
        target_row = -1
        while lo <= hi:
            mid = lo + ((hi-lo)/2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            elif matrix[mid][0] > target:
                hi = mid - 1
            else: 
                lo = mid + 1
        # BST - find column
        lo, hi = 0, len(matrix[target_row]) - 1
        while lo <= hi:
            mid = lo + ((hi-lo)/2)
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False 