"""
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list
Difficulty: medium

Problem:
delete nth node from end

Input / Output:


Notes:


Solution Approaches:
hash-map then remove
alternative (space efficient) would be to have a slow/fast

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head: return head
        cache = {}
        curr, i = head, 1
        while curr:
            cache[i] = curr
            i+=1
            curr = curr.next
        link_to_remove = i-n
        if link_to_remove==1 : return cache[link_to_remove].next
        cache[link_to_remove-1].next = cache[link_to_remove].next
        return head