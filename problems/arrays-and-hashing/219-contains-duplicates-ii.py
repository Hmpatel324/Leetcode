"""
Link: https://leetcode.com/problems/contains-duplicate-ii
Difficulty: easy

Problem:
see if there is a duplicates within k elements

Input / Output:
nums = [1,2,3,1], k = 3 => true

Notes:


Solution Approaches:
preprocess then run through (this is inefficient)
should really on track the last observed - saves o(n)

"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cache = {}
        # Create cache of entries to index
        for i,v in enumerate(nums):
            if v not in cache:
                cache[v] = []
            cache[v] = cache[v] + [i]

        for val in cache.keys():
            val_indexes = cache[val]
            if len(val_indexes) > 1:
                temp = 0
                while temp + 1 < len(val_indexes):
                    if (val_indexes[temp+1] - val_indexes[temp]) <= k:
                        return True
                    temp += 1
        return False