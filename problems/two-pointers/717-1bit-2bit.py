"""
Link: https://leetcode.com/problems/1-bit-and-2-bit-characters
Difficulty: easy

Problem:
Bit options: 0 [1 bit], 10, 11 [2 bit] - determine if last bit is a 1 or 2 bit

Input / Output:


Notes:


Solution Approaches:
Two pointer movement/expansion with tracking last reading frame as one or two bit

"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        fast, slow = 0,0
        is_last_one_bit = False
        while slow < len(bits):
            if bits[slow] == 1:
                is_last_one_bit = False
                fast = slow+1
            else:
                is_last_one_bit = True
                fast = slow
            slow = fast+1
        return is_last_one_bit