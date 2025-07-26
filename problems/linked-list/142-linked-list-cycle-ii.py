"""
Link: https://leetcode.com/problems/linked-list-cycle-ii    
Difficulty: medium

Problem:
Detect a cycle in a LinkedList and return the node

Input / Output:


Notes:


Solution Approaches:
Cache based approach

2p approach, fast = 2x and slow = 1x
then use another from head 1x and slow 1x to find intersection

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cache = set()
        while head:
            if head in cache: return head
            cache.add(head)
            head=head.next
        return