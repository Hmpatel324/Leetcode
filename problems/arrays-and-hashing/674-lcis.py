"""
Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence
Difficulty: easy

Problem:
Find the length of the lognest increasing sub sequence in the array

Input / Output:


Notes:


Solution Approaches:
DP based memoization 

"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        dp = [1] * len(nums)
        index = 1
        while index <= len(nums)-1:
            if nums[index] > nums[index-1]:
                dp[index] = dp[index-1]+1
                res = max(res, dp[index])
            index+=1
        return res