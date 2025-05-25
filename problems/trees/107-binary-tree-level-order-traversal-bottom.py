"""
Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii
Difficulty: medium

Problem:
bottom up level order traversal

Input / Output:


Notes:


Solution Approaches:
Regular Level order with result reversed at end.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        queue = [root]
        while queue:
            curr_level = queue
            queue = None
            next_level, temp = [], []
            for node_entry in curr_level:
                temp.append(node_entry.val)
                if node_entry.left:
                    next_level.append(node_entry.left)
                if node_entry.right:
                    next_level.append(node_entry.right)
            res.append(temp)
            if next_level:
                queue = next_level
        return res[::-1]