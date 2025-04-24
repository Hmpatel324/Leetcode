"""
Link: https://leetcode.com/problems/palindrome-linked-list
Difficulty: easy

Problem:
is a linkedlist a palindrome

Input / Output:


Notes:


Solution Approaches:
Pass #1 - create stack, Pass #2 - pop/compare 

alternative, find middle then reverse second half, then finally compare to first half

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head: return True
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            expected = stack.pop()
            if curr.val != expected:
                return False
            curr = curr.next
        return True
