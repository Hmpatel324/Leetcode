"""
Link: https://leetcode.com/problems/can-place-flowers
Difficulty: Easy

Problem:
Can n flowers be planted given no two flowers can be planted adjacently

Input / Output:


Notes:


Solution Approaches:
DP array approach

"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        dp = [0]*len(flowerbed)
        max_found = 0
        for i,v in enumerate(flowerbed):
            if v == 1:
                dp[i] = 0
            else:
                left = 0 if i==0 else flowerbed[i-1]
                right = 0 if i==len(flowerbed)-1 else flowerbed[i+1]
                if left == 0 and right == 0 and dp[i-1]==0:
                    n-=1
                    dp[i]=1
                else:
                    dp[i] = 0
        return n<=0