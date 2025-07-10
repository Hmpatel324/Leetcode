"""
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist
Difficulty: easy

Problem:
determine if i and 2*i are in a list

Input / Output:


Notes:


Solution Approaches:
Set as a cache to track observed then iterate

"""
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cache = set()
        for i in arr:
            if 2*i in cache or i/2.0 in cache:
                return True
            cache.add(i)
        return False