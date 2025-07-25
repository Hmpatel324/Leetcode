"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
Difficulty: medium

Problem:
Given a string s, find the length of the longest substring without duplicate characters.

Input / Output:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notes:
substring == contiguous

Solution Approaches:
Sliding window via a set approach. Expand and shrink based on inclusion or not in set

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if not s: return res
        curr = set()
        slow, fast = 0,0
        while fast<len(s):
            # Expansion
            if s[fast] not in curr:
                curr.add(s[fast])
                fast+=1
                res = max(res, len(curr))
            # shrink
            else: 
                curr.remove(s[slow])
                slow+=1
        return res