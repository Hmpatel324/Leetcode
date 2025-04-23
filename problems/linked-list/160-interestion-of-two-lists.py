"""
Link: https://leetcode.com/problems/intersection-of-two-linked-lists
Difficulty: east

Problem:
return linkedlist node if two lists intersect

Input / Output:


Notes:


Solution Approaches:
process list A into set based cache then run through b to see if any cache hits

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cache = set()
        curr = headA
        while curr:
            cache.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in cache:
                return curr
            curr = curr.next
        return None