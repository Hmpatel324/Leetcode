"""
Link: https://leetcode.com/problems/assign-cookies
Difficulty: easy

Problem:
assign cookies based on cookie greed factor

Input / Output:


Notes:


Solution Approaches:
Sort both input lists then run move a pointer down both and see how far list1 can move down for values in list 2

"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_index, s_index = 0,0
        res = 0
        while g_index <= len(g)-1 and s_index <= len(s)-1:
            if g[g_index] <= s[s_index]:
                res +=1
                g_index+=1
                s_index+=1
            else:
                s_index +=1
        return res