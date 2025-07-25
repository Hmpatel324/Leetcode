"""
Link: https://leetcode.com/problems/longest-nice-substring
Difficulty: easy

Problem:
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. 
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Input / Output:
Input: s = "YazaAay"
Output: "aAa"

Notes:


Solution Approaches:
Brute Force  

"""
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i,v in enumerate(s):
            temp = i
            observed = set()
            unpaired = set()
            while temp < len(s):
                if 'a'<=s[temp]<='z':
                    if s[temp].upper() in observed:
                        if s[temp].upper() in unpaired: unpaired.remove(s[temp].upper())
                    else:
                        unpaired.add(s[temp])
                else:
                    if s[temp].lower() in observed:
                        if s[temp].lower() in unpaired: unpaired.remove(s[temp].lower())
                    else:
                        unpaired.add(s[temp])
                observed.add(s[temp])
                if (not unpaired) and len(res)<temp-i+1:
                    res = str(s[i:temp+1])
                temp+=1
        return res