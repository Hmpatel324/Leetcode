"""
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Difficulty: easy

Problem:
find first occurance of a substring in mainstring or return -1

Input / Output:


Notes:


Solution Approaches:
Iterate over string and compare to substring

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        curr = 0
        while curr<len(haystack):
            if haystack[curr] == needle[0]:
                temp_curr, i = curr,0
                while i<len(needle):
                    if temp_curr>=len(haystack) or haystack[temp_curr]!=needle[i]:
                        break
                    temp_curr+=1
                    i+=1
                if i==len(needle): return curr
            curr+=1
        return -1