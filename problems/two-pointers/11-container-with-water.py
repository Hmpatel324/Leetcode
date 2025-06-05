"""
Link: https://leetcode.com/problems/container-with-most-water
Difficulty: medium

Problem:
Find window with max water

Input / Output:


Notes:


Solution Approaches:
2p move slow

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        slo, fast = 0, len(height)-1
        while slo != fast:
            curr_area = (fast-slo) * min(height[slo], height[fast])
            res = max(res, curr_area)
            if height[slo] < height[fast]:
                slo +=1
            else:
                fast -=1
        return res
        