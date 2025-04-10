"""
Link: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements
Difficulty: easy

Problem:
given list of nums, remove largest and smallest each cycle and return the smallest average pair

Input / Output:


Notes:


Solution Approaches:
Sort then lo/hi pointer iterate

"""
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        res = float('inf')
        nums.sort()
        lo, hi = 0, len(nums)-1
        while lo < hi:
            res = min(res, float((nums[lo]+nums[hi])/2.0))
            lo +=1
            hi -=1
        return res