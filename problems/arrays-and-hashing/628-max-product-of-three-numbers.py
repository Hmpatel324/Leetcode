"""
Link: https://leetcode.com/problems/maximum-product-of-three-numbers
Difficulty: easy

Problem:
determine max product of 3 numbers in lsit

Input / Output:


Notes:


Solution Approaches:
Sort
Then return max of 0,1,-1 and -1,-2,-3 (two largest neg and largest pos) (all pos)

"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        neg = nums[0]*nums[1]*nums[-1]
        pos = nums[-1]*nums[-2]*nums[-3]
        return max(neg,pos)
        