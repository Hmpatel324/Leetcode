"""
Link: https://leetcode.com/problems/reorder-list
Difficulty: medium

Problem:
Make regular linked list into L1 -> L-1 -> L2 -> L-2... 

Input / Output:


Notes:


Solution Approaches:
Find mid point of LL
Then reverse second half
Then re-assemble

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head,head.next
        if fast:
            # determine mid point
            while fast.next:
                fast = fast.next
                slow = slow.next
                if not fast.next:
                    break
                fast = fast.next
            
            tail_fwd = slow
            tail_rev = slow.next
            head_rev = fast 

            # reverse second half
            slow = tail_rev
            fast = slow.next
            while fast:
                temp = fast
                fast = fast.next
                temp.next = slow
                slow = temp
            
            tail_fwd.next = None
            tail_rev.next = None

            curr = ListNode(0)
            while head and head_rev:
                curr.next = head
                curr = curr.next
                head = head.next
                curr.next = head_rev
                curr = curr.next
                head_rev = head_rev.next
            if head:
                curr.next = head