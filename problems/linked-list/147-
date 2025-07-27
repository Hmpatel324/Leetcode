"""
Link: https://leetcode.com/problems/insertion-sort-list
Difficulty: medium

Problem:
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

Input / Output:


Notes:


Solution Approaches:
Dummy res node
    then insert at either the head, middle, or end of res linked list  
    

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        while head:
            node_to_insert = head
            head = head.next
            node_to_insert.next = None

            # first link to insert
            if not res.next: 
                res.next = node_to_insert
            # insertion occurs at head
            elif node_to_insert.val <= res.next.val:
                node_to_insert.next = res.next
                res.next = node_to_insert
            else:
                temp = res.next
                while temp.next and temp:
                    # Insert in middle
                    if temp.val<node_to_insert.val<=temp.next.val:
                        node_to_insert.next = temp.next
                        temp.next = node_to_insert
                    temp = temp.next
                # insert at end 
                if node_to_insert.val >= temp.val:
                    temp.next = node_to_insert
                    
        return res.next
