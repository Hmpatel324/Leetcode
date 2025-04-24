"""
Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
Difficulty: easy

Problem:
convert a linked list number to a int

Input / Output:
head = [1,0,1] => 5

Notes:


Solution Approaches:
create list of values then foreach over the reversed list

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        res = 0
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        for i,v in enumerate(vals[::-1]):
            res += (v*(2**i))
        return res