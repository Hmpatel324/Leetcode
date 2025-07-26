"""
Link: https://leetcode.com/problems/odd-even-linked-list
Difficulty: medium

Problem:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

Input / Output:
head = [1,2,3,4,5]
[1,3,5,2,4]

Notes:


Solution Approaches:
Create a odd and even linked list then stitch back together

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # setup
        if not head or not head.next: return head
        even = head.next
        curr_odd, curr_even = head, head.next
        slow, fast = head, head.next

        # create even odd LinkedLists
        while slow and fast:
            slow = fast.next
            if not slow or not slow.next: 
                fast = None
                break
            fast = slow.next
            curr_odd.next = slow
            curr_even.next = fast
            curr_odd = curr_odd.next
            curr_even = curr_even.next

        # Account of more odds than evens
        if not fast:
            curr_even.next = None
        if slow:
            curr_odd.next = slow
            curr_odd = curr_odd.next

        # Re-Stitch
        curr_odd.next = even
        return head

