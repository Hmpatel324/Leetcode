"""
Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
Difficulty: easy

Problem:
Find number of negative numbers in a grid 
Note: the grid is sorted inc->dec horizontally and vertically

Input / Output:


Notes:


Solution Approaches:
Modified Binary search with High being passed to next row level on the basis of the prev row first negative instance

"""
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        max_len = len(grid[0])
        hi = max_len-1
        for i in range(len(grid)):
            lo = 0
            neg_found = False
            while lo<=hi:
                mid = lo + ((hi-lo)/2)
                mid_value = grid[i][mid]
                if mid_value<0 and (mid==0 or grid[i][mid-1]>=0):
                    res += (max_len if mid==0 else (max_len - mid))
                    hi = mid
                    neg_found = True
                    break
                elif mid_value>=0:
                    lo = mid+1
                else:
                    hi = mid-1
            if not neg_found: hi = max_len-1
        return res
            

