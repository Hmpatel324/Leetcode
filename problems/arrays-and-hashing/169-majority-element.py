"""
Link: https://leetcode.com/problems/majority-element
Difficulty: easy

Problem:
given list of ints, find the highest frequency item and return it

Input / Output:
[3,2,3] => 3
[2,2,1,1,1,2,2] => 2

Notes:


Solution Approaches:
count dictionary then iterate through and find highest count

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = Counter(nums)
        print(cache)
        res, freq = -1,0
        for i in cache.keys():
            k = cache[i]
            if k > freq:
                freq = k
                res = i
        return res