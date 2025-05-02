"""
Link: https://leetcode.com/problems/guess-number-higher-or-lower
Difficulty: easy

Problem:
Guess correct number given a range of numbers

Input / Output:


Notes:


Solution Approaches:
Binary Search

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + ((hi-lo)/2)
            mid_res = guess(mid)
            if mid_res == 0:
                return mid
            elif mid_res==1:
                lo = mid+1
            else:
                hi = mid-1
        return hi