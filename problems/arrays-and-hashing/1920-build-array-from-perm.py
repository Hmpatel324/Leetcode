"""
Link: https://leetcode.com/problems/build-array-from-permutation
Difficulty: easy

Problem:
build new array given below formula

Input / Output:
[0,2,1,5,3,4] => [0,1,2,4,5,3]

Notes:


Solution Approaches:
build static list of zeros and map in values

"""
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        i = 0
        while i < len(nums):
            res[i] = nums[nums[i]]
            i+=1
        return res