"""
Link: https://leetcode.com/problems/binary-search
Difficulty: easy

Problem:
implement binary search

Input / Output:


Notes:

Solution Approaches:
1) find mid 2) match target 3) shift frame depending on if mid is greater or less than target

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + ((hi - lo)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1