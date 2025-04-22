"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list
Difficulty: easy

Problem:
remove duplicates from a sorted linked list

Input / Output:


Notes:


Solution Approaches:
Fast/slow pointer. Follow pattern for accordian expansion and contraction.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return head
        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return head