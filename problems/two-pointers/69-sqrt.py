"""
Link: https://leetcode.com/problems/sqrtx
Difficulty: easy

Problem:
find rounded down sqrt of a input

Input / Output:


Notes:


Solution Approaches:
2p binary search

"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 0, x+1
        while(lo<=hi):
            mid = lo + ((hi-lo)/2)
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                hi = mid-1
            else:
                lo = mid+1
        return hi
        