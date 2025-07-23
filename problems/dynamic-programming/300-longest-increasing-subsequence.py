"""
Link: https://leetcode.com/problems/longest-increasing-subsequence
Difficulty: medium

Problem:
find longest increasing subsequence (means not necessarily CONTIGUOUS)

Input / Output:


Notes:


Solution Approaches:
DP array + brute force iteration

"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        local_max = -float('inf')
        res = 1
        for i,v in reversed(list(enumerate(nums))):
            if v>local_max:
                local_max = max(local_max,v)
            else:
                for j in range(i,len(nums)):
                    if nums[j]>v:
                        dp[i]=max(dp[j]+1, dp[i])
        return max(dp)