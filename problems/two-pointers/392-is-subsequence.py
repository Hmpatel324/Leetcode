"""
Link: https://leetcode.com/problems/is-subsequence
Difficulty: easy

Problem:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.


Input / Output:
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Notes:


Solution Approaches:
2-p, concurrent attempts to move

"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        curr_s = 0
        curr_t = 0
        while curr_t<len(t) and curr_s<len(s):
            if s[curr_s]==t[curr_t]:
                curr_s+=1
            curr_t+=1
        return curr_s==len(s)