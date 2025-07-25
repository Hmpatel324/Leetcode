"""
Link: https://leetcode.com/problems/alternating-groups-i/
Difficulty: easy

Problem:
There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Input / Output:

colors = [1,1,1]
0

[0,1,0,0,1]
3

Notes:


Solution Approaches:
Sliding window of 3 
Special edge case for index 0 and -1 as it wraps around

"""
class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        res = 0
        if not colors: return res
        
        # edge case - index 0
        if colors[1]==colors[-1] and colors[1]!=colors[0]: res+=1
        #edge case - index -1
        if colors[-2]==colors[0] and colors[0]!=colors[-1]: res+=1
        
        #remainder
        for j in range(1,len(colors)-1):
            if colors[j-1]==colors[j+1] and colors[j]!= colors[j-1]: res+=1
        
        return res