"""
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree
Difficulty: easy

Problem:
Find shorthest depth to a leaf

Input / Output:


Notes:


Solution Approaches:
BFS and find first instance of a leaf 
Use tuple (node, depth) in the bfs queue

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        queue = [(root,0)]
        while queue:
            curr_node, curr_depth = queue.pop(0)
            if not curr_node.left and not curr_node.right:
                return curr_depth+1
            if curr_node.left:
                queue.append((curr_node.left, curr_depth+1))
            if curr_node.right:
                queue.append((curr_node.right, curr_depth+1))
        return -1