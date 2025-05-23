"""
Link: https://leetcode.com/problems/plus-one
Difficulty: easy

Problem:
Add 1 to input number as aigits and return the value

Input / Output:


Notes:


Solution Approaches:
Seed in the +1 via the seeded remainder. Determine new digit via modulus 10 and determine remainder via /10

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        remainder = 1
        index = len(digits)-1
        while index>=0:
            total = digits[index]+remainder
            digits[index]=total%10
            remainder = total/10
            index-=1
        return [1]+digits if remainder==1 else digits