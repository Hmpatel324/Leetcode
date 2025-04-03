"""
Link: https://leetcode.com/problems/range-sum-query-immutable
Difficulty: easy

Problem:
Given list of nums, implement class to return sum given left/right inclusive

Input / Output:
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]] => [null, 1, -1, -3]

Notes:


Solution Approaches:
DP array in constructor
Then return right - 1 before left

"""

class NumArray(object):

    dp = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]*len(nums)
        for i,v in enumerate(nums):
            self.dp[i] = self.dp[i-1]+v if i>0 else v
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.dp[right]-(self.dp[left-1] if left > 0 else 0)
