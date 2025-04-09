"""
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree
Difficulty: easy

Problem:
find max height of a tree

Input / Output:


Notes:


Solution Approaches:
Iterative breadth first parse of tree. Use tuple to with height second pair to track depth.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        res = 1
        queue = [(root,1)]
        while queue:
            curr_node, curr_depth = queue.pop(0)
            res = max(curr_depth, res)
            if curr_node.left:
                queue.append((curr_node.left, curr_depth+1))
            if curr_node.right:
                queue.append((curr_node.right, curr_depth+1))
        return res