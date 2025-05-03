"""
Link: https://leetcode.com/problems/valid-perfect-square
Difficulty: easy

Problem:
determine if param, num, is a perfect square

Input / Output:


Notes:


Solution Approaches:
Binary search with 0/num as lo/hi

"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 0, num
        while lo<=hi:
            mid = lo + ((hi-lo)/2)
            mid_sq = mid**2
            if mid_sq == num:
                return True
            elif mid_sq > num:
                hi = mid-1
            else:
                lo = mid+1
        return False
