"""
Link: https://leetcode.com/problems/remove-linked-list-elements
Difficulty: easy

Problem:
Remove all instances of a particular value 

Input / Output:


Notes:


Solution Approaches:
slow/fast to remove and redirect slow.next

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head: return head
        res = ListNode()
        res.next = head
        slow, fast = res, head
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return res.next