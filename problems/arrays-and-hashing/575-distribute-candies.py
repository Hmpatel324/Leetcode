"""
Link: https://leetcode.com/problems/distribute-candies
Difficulty: easy

Problem:
Given List of available candies, determine max variations permitted

Input / Output:


Notes:


Solution Approaches:
Create Count Dict to determine number of vars, then return min of vars and total avail/2

"""
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        cache = Counter(candyType)
        return min(len(candyType)/2, len(cache))