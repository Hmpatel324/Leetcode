"""
Link: https://leetcode.com/problems/valid-palindrome
Difficulty: easy

Problem:
is a string a palindrome - case not withstanding

Input / Output:


Notes:


Solution Approaches:
add letters to a stack then re run through string

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s.lower():
            if "a"<=i<="z" or "0"<=i<="9":
                stack.append(i)
        if not stack: return True
        for i in s.lower():
            if "a"<=i<="z" or "0"<=i<="9":
                curr = stack.pop()
                if i != curr:
                    return False
        return True
