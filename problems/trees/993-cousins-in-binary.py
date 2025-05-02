"""
Link: https://leetcode.com/problems/cousins-in-binary-tree
Difficulty: easy

Problem:
Determine if x and y are "cousins" == same level with diff parents

Input / Output:


Notes:


Solution Approaches:
Breadth first search for scan then determine if cousins

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_meta, y_meta = None, None
        stack = [(root, 0, None)]
        while stack:
            curr_node, curr_level, curr_parent = stack.pop(0)
            if curr_node.val == x:
                x_meta = (curr_level, curr_parent)
            if curr_node.val == y:
                y_meta = (curr_level, curr_parent)
            if x_meta and y_meta: break
            if curr_node.left:
                stack.append((curr_node.left, curr_level+1, curr_node))
            if curr_node.right:
                stack.append((curr_node.right, curr_level+1, curr_node))
        return True if x_meta[0]==y_meta[0] and x_meta[1]!=y_meta[1] else False