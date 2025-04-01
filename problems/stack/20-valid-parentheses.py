"""
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: east

Problem:
check if a string has valid paranthesis 

Input / Output:
"()" => true
"()[]{}" => true
"(]" => false
"([])" => true

Notes:


Solution Approaches:
use a stack to track opens and pop off to track closing the opens

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_lookup = {')':'(', '}':'{', ']':'['}
        open_lookup = {'(', '{', '['}
        validation_stack = []

        for item in s:
            if item in open_lookup:
                validation_stack.append(item)
            else:
                last = validation_stack.pop() if len(validation_stack)>0 else ""
                if last != close_lookup[item]:
                    return False
        return True if len(validation_stack)==0 else False