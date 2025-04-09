"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
Difficulty: easy

Problem:
find the max buy and sell window

Input / Output:
[7,1,5,3,6,4] => 5

Notes:


Solution Approaches:
reverse iterate list, find local max and look for greatest diff

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res, local_max = 0, -1
        for v in prices[::-1]:
            local_max = max(local_max,v)
            res = max(res,local_max-v)
        return res