"""
Link: https://leetcode.com/problems/delete-node-in-a-linked-list
Difficulty: medium

Problem:
Input node is the node to delete, delete it

Input / Output:


Notes:


Solution Approaches:
- Rearrange pointers. Node val=next node val and node next = node.next.next thereby circumventing the next node

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next