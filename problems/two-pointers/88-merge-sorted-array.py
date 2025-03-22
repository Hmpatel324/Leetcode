"""
Link: https://leetcode.com/problems/merge-sorted-array
Difficulty: easy

Problem: 
Merge two already sorted arrays *in place* 

Input / Output:
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 => nums1 at conclusion: [1,2,2,3,5,6]
nums1 = [1], m = 1, nums2 = [], n = 0 => nums1 at conclusion: [1]
nums1 = [0], m = 0, nums2 = [1], n = 1 => nums 1 at conclusion [1]

Notes:
Need to account for in place requirement as well as not override existing num1 *needed* values

Solution Approaches:
- multi-pointer approach from tail
- brute force would consist of merging then shifting _all_ entries back

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        index_1, index_2, write_index = m-1, n-1, m+n-1
        while index_1 >= 0 or index_2 >= 0:
            if index_1 < 0:
                nums1[write_index] = nums2[index_2]
                index_2-=1
            elif index_2 < 0:
                nums1[write_index] = nums1[index_1]
                index_1-=1
            elif nums1[index_1] > nums2[index_2]:
                nums1[write_index] = nums1[index_1]
                index_1-=1
            else:
                nums1[write_index] = nums2[index_2]
                index_2-=1
            write_index -=1



