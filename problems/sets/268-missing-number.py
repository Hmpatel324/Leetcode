"""
Link: https://leetcode.com/problems/missing-number
Difficulty: easy

Problem:
Given int list of size n, find the missing element

Input / Output:
[3,0,1] => 2
[0,1] => 2

Notes:


Solution Approaches:
- remove from a Set based cache and remove items.
- cache set - nums set

"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = set(range(0,len(nums)+1))
        for i in nums:
            cache.remove(i)
        return cache.pop()

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = set(range(0,len(nums)+1))
        return (cache-set(nums)).pop()