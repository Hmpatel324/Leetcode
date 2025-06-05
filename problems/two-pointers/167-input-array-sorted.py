"""
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: medium

Problem:
Given a sorted int list, return index of two numbers that return sum

Input / Output:


Notes:


Solution Approaches:
Key is that list is sorted
therefore have a slow (0) and fast(len-1) pointers and slide pointers based on curr sum per turn

"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        slo, fast = 0, len(numbers)-1
        while True:
            curr_sum = numbers[slo] + numbers[fast]
            if curr_sum == target: return [slo+1, fast+1]
            elif curr_sum < target: slo+=1
            else: fast -= 1
        return []
        