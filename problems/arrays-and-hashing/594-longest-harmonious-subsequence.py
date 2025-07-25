"""
Link: https://leetcode.com/problems/longest-harmonious-subsequence
Difficulty: easy

Problem:
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

Input / Output:
[1,3,2,2,5,2,3,7]
5

[1,1,1,1]
0

[1,2,3,4]
2

Notes:


Solution Approaches:
Key point is that it is a subsequence so items can be skipped
effectivley it turns into a counting problem due to the skipping

"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = 0
        cache = Counter(nums)
        for key in cache:
            hi = cache.get(key+1,0)
            lo = cache.get(key-1,0)
            direction = max(hi,lo)
            if direction!=0: res = max(res, cache[key]+direction)
        return res
