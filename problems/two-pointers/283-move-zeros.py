"""
Link: https://leetcode.com/problems/move-zeroes
Difficulty: easy

Problem:
move zeros in a list to end while maintaining relative order and doing inplace

Input / Output:
[0,1,0,3,12] => [1,3,12,0,0]

Notes:


Solution Approaches:
slow point for reading frame and use fast for exploration

"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while(fast < len(nums)):
            if nums[slow]==0 and nums[fast]!=0:
                nums[slow] = nums[fast]
                nums[fast] = 0
                slow += 1
            elif nums[slow]==0 and nums[fast]==0:
                fast+=1
            else:
                slow+=1
                fast = slow