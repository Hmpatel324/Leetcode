"""
Link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i
Difficulty: easy

Problem:
Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
return number of operations

Input / Output:
[5,2,3,1] => 2

Notes:


Solution Approaches:
Brute Force: do the ops

"""
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        while len(nums) > 1:
            inorder = True
            i = 1
            min_sum, min_sum_index = float('inf'), -1
            while i < len(nums):
                curr_sum = nums[i] + nums[i-1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    min_sum_index = i
                if nums[i-1] > nums[i]:
                    inorder = False
                i+=1
            if inorder: return res
            res+=1
            nums = nums[0:min_sum_index-1] + [min_sum] + nums[min_sum_index+1:]
        return res