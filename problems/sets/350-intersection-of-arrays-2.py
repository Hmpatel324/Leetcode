"""
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii
Difficulty: easy

Problem:
Find intersection of two arrays _including_ quantity of intersection

Input / Output:
nums1 = [1,2,2,1], nums2 = [2,2] => [2,2]

Notes:


Solution Approaches:
1) convert to count dict 2) determine common keys 3) build result

"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Generate Count dictionaries 
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        # determine commonalities
        common_keys = set(c1.keys()) and set(c2.keys())
        # construct result
        res = []
        for key in common_keys:
            res.extend([key]*(c1[key] if c1[key]<c2[key] else c2[key]))
        return res