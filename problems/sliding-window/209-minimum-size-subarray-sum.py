"""
Link: https://leetcode.com/problems/minimum-size-subarray-sum
Difficulty: medium

Problem:
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Input / Output:
target = 7, nums = [2,3,1,2,4,3]
2

Notes:


Solution Approaches:
Pre validate the list for no solution or total array as solution
Then use sliding window to expand and shrink window in order to find optimal subarray len

"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Pre-Validations to shortcut
        total_sum = sum(nums)
        if total_sum<target: return 0
        if total_sum==target: return len(nums)

        # Viable solution within array
        slow,fast = 0,0
        curr_sum = nums[0]
        res = float('inf')
        while slow<=len(nums)-1:
            if curr_sum<target and fast<len(nums)-1:
                fast+=1
                curr_sum+=nums[fast]
            else:
                if curr_sum>=target: res = min(fast-slow+1,res)
                curr_sum-=nums[slow]
                slow+=1
        return res