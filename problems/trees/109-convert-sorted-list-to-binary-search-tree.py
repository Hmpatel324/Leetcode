"""
Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
Difficulty: medium

Problem:
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.


Input / Output:


Notes:


Solution Approaches:
Output as list then use Binary Search (mid-left-right) to build tree

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head: return None
        nums = []
        # Output Linked List as List
        while head:
            nums.append(head.val)
            head=head.next
        res=TreeNode()

        # Build Tree
        # Breadth first explortation/fill in via Binary Sort of outputted list
        queue = [(res,nums)]
        while queue:
            curr, pool = queue.pop(0)
            if pool:
                lo, hi = 0, len(pool)-1
                mid = lo+((hi-lo)/2)
                curr.val = pool[mid]
                left_pool, right_pool = pool[:mid], pool[mid+1:]
                if left_pool:
                    left_node = TreeNode()
                    curr.left = left_node
                    queue.append((left_node,left_pool))
                if right_pool:
                    right_node = TreeNode()
                    curr.right = right_node
                    queue.append((right_node,right_pool))
        return res
