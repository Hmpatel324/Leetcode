"""
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list
Difficulty: medium

Problem:
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input / Output:


Notes:


Solution Approaches:
Pre-order traversal the tree via a stack / output to a list

Iterate over list and update right pointer / set left to None

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        res = []
        if not root: return root

        stack = [root]
        # Parse Tree
        while stack:
            curr_node = stack.pop()
            res.append(curr_node)
            if curr_node.right: stack.append(curr_node.right)
            if curr_node.left: stack.append(curr_node.left)
        
        # Stitch together Linked List
        for i,v in enumerate(res):
            if i == len(res)-1: 
                v.right = None
            else:
                v.right = res[i+1]
            v.left = None
        
        return root