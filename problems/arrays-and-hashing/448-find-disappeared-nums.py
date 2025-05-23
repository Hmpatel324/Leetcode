"""
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
Difficulty: easy

Problem:
find numbers not input array that is not in 1 to len(nums)

Input / Output:


Notes:


Solution Approaches:
Create range, convert input into a set, and then iterate/add over range 

"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        expected = range(1,len(nums)+1)
        nums = set(nums)
        for i in expected:
            if i not in nums:
                res.append(i)
        return res