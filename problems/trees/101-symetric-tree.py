"""
Link: https://leetcode.com/problems/symmetric-tree
Difficulty: easy

Problem:
Determine if a tree is symetric down the middle

Input / Output:


Notes:


Solution Approaches:
Iterate over the tree via BFS.
Use tuple and checks to determine if expected nodes are equal

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root or (not root.left and not root.right): return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if not left or not right or left.val!=right.val:
                return False
            if left.left or right.right:
                queue.append((left.left, right.right))
            if left.right or right.left:
                queue.append((left.right, right.left))
        return True