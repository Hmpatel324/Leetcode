"""
Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list
Difficulty: medium

Problem:
Given a int value K, swap k fwd and k index from end in the linked list

Input / Output:


Notes:


Solution Approaches:
Pass #1 - find k fwd and total len
Pass #2 - find kth from end
Swap value

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head: return head
        fwd = ListNode()
        len = 0
        curr = head
        while curr:
            len += 1
            if len == k:
                fwd = curr
            curr = curr.next
        rev_index = len - k
        curr = head
        while rev_index > 0:
            rev_index-=1
            curr = curr.next
        curr.val , fwd.val = fwd.val, curr.val
        return head
