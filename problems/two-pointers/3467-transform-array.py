"""
Link: https://leetcode.com/problems/transform-array-by-parity
Difficulty: easy

Problem:
Given list of ints, convert odds to 1 and evens to 0 then sort

Input / Output:
[4,3,2,1] => [0,0,1,1]

Notes:


Solution Approaches:
secondary array with a hed and tail pointer to place in mapped values

"""
class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        zero, one = 0, -1
        for i in nums:
            if i%2 == 1:
                res[one] = 1
                one -=1
            else: 
                zero += 1
        return res
