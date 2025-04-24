"""
Link: https://leetcode.com/problems/middle-of-the-linked-list
Difficulty: easy

Problem:
find middle of linked list

Input / Output:


Notes:


Solution Approaches:
slow/fast - move fast 2x vs slow 1x

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow