"""
Link: https://leetcode.com/problems/max-consecutive-ones
Difficulty: easy

Problem:
Given binary list, find max consecutive ones substring *size*

Input / Output:
[1,1,0,1,1,1] => 3

Notes:


Solution Approaches:
2 pointer iteration with a search and window expand arch

"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0,0
        res = 0
        while fast < len(nums):
            # incremement right to find 1 reading frame
            if nums[slow] == 0:
                slow = fast
            # slow on a 1 reading frame, check if end of frame    
            elif nums[fast] == 0:
                res = max(res, fast-slow)
                slow = fast
            # slow on a 1 reading frame, continue expansion
            fast += 1
        # end of reading frame check
        res = max(res, fast-slow) if nums[slow] == 1 and nums[fast-1] == 1 else res
        return res
        