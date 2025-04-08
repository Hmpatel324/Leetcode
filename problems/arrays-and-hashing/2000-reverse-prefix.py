"""
Link: https://leetcode.com/problems/reverse-prefix-of-word
Difficulty: easy

Problem:
given string word and a char, flip from 0 to char OR return original if no char

Input / Output:
"abcdefd", ch = "d" => "dcbaefd"

Notes:


Solution Approaches:
1) Scan for instance 2) return constructed string using slicing

"""
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        # scan for first instance
        detect = -1
        for i,v in enumerate(word):
            if v == ch:
                detect = i
                break
        if detect == -1: return word
        # reconstruct and return
        return word[detect::-1]+word[detect+1:]