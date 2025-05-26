"""
Link: https://leetcode.com/problems/set-mismatch
Difficulty: easy

Problem:
Find the dup item in nums and the ommitted item

Input / Output:


Notes:


Solution Approaches:
1. two sets, a observed set (added to) to find the clash and a expected one (removed from)
"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        corr_set = set(range(1,len(nums)+1))
        curr_set = set()
        res = []
        for i in nums:
            if i in curr_set:
                res.append(i)
            curr_set.add(i)
            if i in corr_set:
                corr_set.remove(i)
        res.append(corr_set.pop())
        return res