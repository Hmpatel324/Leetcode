"""
Link: https://leetcode.com/problems/search-insert-position
Difficulty: easy

Problem:
find where to insert via bst algo

Input / Output:


Notes:


Solution Approaches:
bst 

"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while(lo<=hi):
            mid = lo + ((hi-lo)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                hi = mid-1
            else:
                lo = mid+1
        return lo