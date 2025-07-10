"""
Link: https://leetcode.com/problems/find-peak-element
Difficulty: medium

Problem:
Find peak and return index

Input / Output:


Notes:


Solution Approaches:
Modified binary search
*indication to do so was log n eff

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0

        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo + ((hi-lo)/2)
            if mid == 0 and nums[mid+1]<nums[mid]: return mid
            if mid == 0 and nums[mid+1]>nums[mid]: lo = mid+1
            elif mid == len(nums)-1 and nums[mid-1]<nums[mid]: return mid
            elif mid == len(nums)-1 and nums[mid-1]>nums[mid]: hi = mid-1
            elif nums[mid-1]<nums[mid]>nums[mid+1]: return mid
            elif nums[mid-1]<nums[mid]<nums[mid+1]: lo = mid+1
            else: hi = mid-1
        return -1