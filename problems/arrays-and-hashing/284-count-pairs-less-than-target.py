"""
Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target
Difficulty: easy

Problem:
pairs sum is less than target

Input / Output:
nums = [-1,1,2,3,1], target = 2 => 3

Notes:


Solution Approaches:
Brute Force

"""
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for i,k in enumerate(nums):
            for j in nums[i+1:]:
                if k+j < target:
                    res += 1
        return res