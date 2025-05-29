"""
Link: https://leetcode.com/problems/binary-tree-paths
Difficulty: easy

Problem:
Output as strings root to leaf path 

Input / Output:


Notes:


Solution Approaches:
BFS with queue consisting of tuple (node, path)

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        if not root: return res
        queue = [(root, "")]
        while queue:
            curr_node, curr_path = queue.pop(0)
            curr_path = curr_path+str(curr_node.val)
            if curr_node.left:
                queue.append((curr_node.left, curr_path+"->"))
            if curr_node.right:
                queue.append((curr_node.right, curr_path+"->"))
            if not curr_node.left and not curr_node.right:
                res.append(curr_path)
        return res