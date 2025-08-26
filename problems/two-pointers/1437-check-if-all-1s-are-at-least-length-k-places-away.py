"""
Link: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away
Difficulty: easy

Problem:
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

Input / Output:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true

Notes:


Solution Approaches:
track distance from curr 1 to previous ==1

"""
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        slow = 0 
        last_found =-float('inf')
        while slow<len(nums):
            if nums[slow]==1:
                if slow-last_found-1<k: return False
                last_found=slow
            slow+=1
        return True