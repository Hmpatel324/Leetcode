"""
Link: https://leetcode.com/problems/add-two-numbers
Difficulty: medium

Problem:


Input / Output:


Notes:


Solution Approaches:
Keep a running remainder (init at 0) and create a total per unit then push both ll to exhaustion. Finally optionally add final link. 

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        curr_res = res
        remainder = 0
        while l1 or l2:
            temp = remainder
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            remainder = (temp - (temp % 10))/10
            curr_res.next = ListNode(temp - 10*remainder)
            curr_res = curr_res.next
        if remainder > 0:
            curr_res.next = ListNode(remainder)
        return res.next
