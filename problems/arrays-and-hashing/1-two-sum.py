"""
Link: https://leetcode.com/problems/two-sum
Difficulty: easy

Problem:
Given list of integers, return *indicies* of the two numbers such they add to a target

Input / Output:


Notes:
[2,7,11,15], target = 9 => [0,1] bc 2+7
[3,2,4], target = 6 => [1,2] bc 2+4
nums = [3,3], target = 6 => [0,1] bc 3+3

Solution Approaches:
Need to recall previous while continuing to move pointer fwd; however, need to recall index as well therefore dictionary {value : index}

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {} # initialize cache
        for index,item in enumerate(nums):
            required_val = target - item
            if required_val in cache: return [cache[required_val], index]
            cache[item] = index

