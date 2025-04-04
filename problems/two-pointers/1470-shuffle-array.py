"""
Link: https://leetcode.com/problems/shuffle-the-array
Difficulty: easy

Problem:
Given a list of ints, split and shuffle into a new list of ints

Input / Output:
nums = [2,5,1,3,4,7], n = 3 => [2,3,5,4,1,7] 

Notes:


Solution Approaches:
left sub list and right sub list pointer with a third reading frame pointer
slide points to populate result

"""
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        left, right = 0, n
        reading_frame = 0
        res = [0] * len(nums)
        while reading_frame < len(nums):
            res[reading_frame] = nums[left]
            res[reading_frame+1] = nums[right]
            reading_frame += 2
            left += 1
            right += 1
        return res