"""
Link: https://leetcode.com/problems/contains-duplicate
Difficulty: Easy

Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input / Output:
[1,2,3,1] -> true | bc of 1
[1,2,3,4] -> false | bc of no dups
[1,1,1,3,3,4,3,2,4,2] -> true | bc of 2

Notes:
List can be unsorted 

Solution Approaches:
- HashSet "cache" of observed while iterating. True if clash else false. 
Use of Hashset for lookup time.

- Brute force approach - For each item then for each element
- Convert List to Set and compare sizes 
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        cache = set() # Empty cache hashset
        for entry in nums:
            if entry in cache:
                return True
            cache.add(entry)
        return False
    