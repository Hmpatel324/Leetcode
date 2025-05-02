"""
Link: https://leetcode.com/problems/count-complete-tree-nodes
Difficulty: easy

Problem:
count number of nodes in a tree

Input / Output:


Notes:


Solution Approaches:
Breadth first search

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = 0
        if not root: return res
        queue = [root]
        while queue: 
            curr = queue.pop(0)
            res += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return res