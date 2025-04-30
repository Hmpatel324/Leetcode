"""
Link: https://leetcode.com/problems/first-bad-version
Difficulty: easy

Problem:
given n attempts, determine attempt # which flipped attempts from false to true

Input / Output:


Notes:


Solution Approaches:
binary search

"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + ((hi-lo)/2)
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid-1):
                    return mid
                else:
                    hi = mid-1
            else:
                lo = mid+1
        return lo