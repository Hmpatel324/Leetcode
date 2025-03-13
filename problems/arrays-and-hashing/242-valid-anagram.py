"""
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: easy

Problem
Given two strings s and t, are they anagrams

Input / Output:
s = "anagram", t = "nagaram" => true
s = "rat", t = "car" => false due to c

Notes:
Anagram consists of rearranging all letters
Observation imple hashset does NOT account for multiple letters therefore need dictionary {char : frequency}

Solution Approaches:
- Convert one string into a frequency dictionary and iterate/pop off. If fail lookup then return false, else true
- Convert both to count dictionary and compare counts
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = set(Counter(s).items())
        t = set(Counter(t).items())
        if(len(s)!=len(t)):
            return False
        for each in s:
            if(each not in t):
                return False
        return True