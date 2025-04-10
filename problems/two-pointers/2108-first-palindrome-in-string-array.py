"""
Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array
Difficulty: easy

Problem:
Find first instande of palindrome in a list of strings 

Input / Output:
["abc","car","ada","racecar","cool"] => "ada"

Notes:


Solution Approaches:
- iterate through list and use hi/lo 2p approach to test using breaks to save on unnecessary comparisons
- alternate of 2p approach for test would be string compare

"""
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = str()
        for w in words:
            lo, hi = 0, len(w)-1
            while(lo <= hi):
                if w[lo] != w[hi]:
                    break
                lo+=1
                hi-=1
            if lo > hi:
                res = w
                break
        return res

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = str()
        for w in words:
            if w == w[::-1]:
                res = w
                break
        return res