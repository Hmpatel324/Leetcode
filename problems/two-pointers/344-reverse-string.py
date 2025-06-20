"""
Link: https://leetcode.com/problems/reverse-string
Difficulty: easy

Problem:
reverse a string

Input / Output:


Notes:


Solution Approaches:
Given constraint of 0(1) space, 2p flip

"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lo, hi = 0, len(s)-1
        while lo<hi:
            s[lo],s[hi]=s[hi],s[lo]
            lo+=1
            hi-=1
            