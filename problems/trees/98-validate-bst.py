"""
Link: https://leetcode.com/problems/validate-binary-search-tree
Difficulty: medium

Problem:
Validate the provided BST

Input / Output:


Notes:


Solution Approaches:
Iterative BFS. 
In the queue pass tuple (node, lower-bound, upper-bound)
If node value is not in range then return false
If Left: update upper-bound to node value
If Right: update lower-bound to node value

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root: return True
        queue = [(root, -float('inf'), float('inf'))]
        while queue:
            node, lb, ub = queue.pop(0)
            if not lb < node.val < ub:
                return False
            if node.left: queue.append((node.left, lb, node.val))
            if node.right: queue.append((node.right, node.val, ub))
        return True