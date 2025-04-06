"""
Link: https://leetcode.com/problems/reverse-linked-list
Difficulty: easy

Problem:
reverse a linked list

Input / Output:


Notes:


Solution Approaches:
Essentially use a temp node and flip the next pointer of nodes

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # null check
        if head == None: return head
        slow = head
        fast = slow.next
        slow.next = None
        while fast!= None:
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp
        return slow