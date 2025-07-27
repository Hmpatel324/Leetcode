"""
Link: https://leetcode.com/problems/reverse-linked-list-ii
Difficulty: medium

Problem:
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input / Output:
head = [1,2,3,4,5], left = 2, right = 4
[1,4,3,2,5]

Notes:


Solution Approaches:
Need a slow/fast for left and right
Start Restitching and reverse then finish restitching
Edge Case if left is at 1 essentially

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        if left==right: return head

        # setup
        curr = head
        right_fast, right_slow = None, None
        left_fast, left_slow = None, None

        # locate reverse segment
        index = 1
        while curr:
            if index==left:
                left_fast = curr
            if not left_fast:
                left_slow = curr
            if index==right:
                right_fast = curr
            if not right_fast:
                right_slow = curr
            curr = curr.next
            index+=1
        
        # Not found - return original
        if not left_fast or not right_fast: return head

        # print(left_slow.val)


        # reverse and restitch

        if left_slow:
            left_slow.next = right_fast
        tail = left_fast

        slow,fast = left_fast, left_fast.next
        while slow!= right_fast:
            temp = fast
            fast = fast.next
            temp.next = slow
            slow = temp
        
        tail.next = fast

        return head if left_slow else right_fast


