"""
Link: https://leetcode.com/problems/range-addition-ii
Difficulty: easy

Problem:
Find area of matrix with highest value

Input / Output:


Notes:


Solution Approaches:
Find common applicable x/y over all ops

"""
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        max_y = n
        max_x = m
        for i in ops:
            max_y = min(max_y, i[1])
            max_x = min(max_x, i[0])
        return max_y*max_x