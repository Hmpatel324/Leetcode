"""
Link: https://leetcode.com/problems/reverse-vowels-of-a-string
Difficulty: easy

Problem:
return input string with all vowels reversed

Input / Output:


Notes:


Solution Approaches:
use a set with vowels
use 2p to slide up and down then flip

"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a','e','i','o','u'}
        lo, hi = 0, len(s)-1
        s = list(s)
        while lo<hi:
            if s[lo].lower() not in vowels:
                lo+=1
            if s[hi].lower() not in vowels:
                hi-=1
            if s[lo].lower() in vowels and s[hi].lower() in vowels:
                s[lo],s[hi]=s[hi],s[lo]
                hi-=1
                lo+=1
        return str().join(s)
