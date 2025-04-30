"""
Link: https://leetcode.com/problems/swap-nodes-in-pairs
Difficulty: medium

Problem:
swap pairs of nodes

Input / Output:


Notes:


Solution Approaches:
3 pointers: anchor, slow, fast then redirect the nexts to flow from anchor->fast->slow->og fast.next

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        res.next = head
        curr_res = res
        if not head: return res.next
        if not head.next: return head
        while curr_res:
            slow, fast = None, None
            slow = curr_res.next
            if slow: fast = slow.next
            if not slow or not fast: break
            true_next = fast.next
            curr_res.next = fast
            fast.next = slow
            slow.next = true_next
            curr_res = slow
        return res.next