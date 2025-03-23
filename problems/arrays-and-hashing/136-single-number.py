"""
Link: https://leetcode.com/problems/single-number
Difficulty: Easy

Problem:
Find the unique item in a list of numbers given there are two of everthing else

Input / Output:
[2,2,1] => 1

Notes:


Solution Approaches:
Create a observed items struct via a set and remove items on a second appearance ie stack

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = set()
        for i in nums:
            if i in cache:
                cache.remove(i)
            else:
                cache.add(i)
        return cache.pop()