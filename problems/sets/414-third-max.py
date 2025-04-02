"""
Link: https://leetcode.com/problems/third-maximum-number
Difficulty: easy

Problem:
Find third largest (or largest if len<3) in a int list excluding dups

Input / Output:
[3,2,1] => 1
[1,2] => 2

Notes:


Solution Approaches:
make into set then sort

"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = list(set(nums))
        unique.sort()
        return unique[-3] if len(unique) >= 3 else unique[-1]