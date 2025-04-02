"""
Link: https://leetcode.com/problems/intersection-of-two-arrays
Difficulty: easy

Problem:
find intersection of arrays and result should be unique

Input / Output:
[1,2,2,1] [2,2] => [2]

Notes:


Solution Approaches:
return intersection of sets

"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))