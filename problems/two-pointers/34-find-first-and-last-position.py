"""
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
Difficulty: med

Problem:
Given SORTED list return the first and last of target value instances in the input

Input / Output:


Notes:


Solution Approaches:
Binary Search for target lower index then slide up for upper
Option 2 (more efficient?) Above but instead of sliding up for upper re-run bst for upper

"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums)-1
        res = [-1,-1]

        while lo<=hi:
            mid = lo + ((hi-lo)/2)
            if nums[mid] == target and (mid==0 or nums[mid-1]!=target):
                res[0] = mid
                break
            elif nums[mid]>= target:
                hi = mid-1
            else:
                lo = mid+1

        # case: target found 
        if res[0]!=-1:
            i = res[0]
            while i<len(nums) and nums[i] == target:
                i += 1
            res[1] = i-1
        return res