"""
Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Difficulty: easy

Problem:
minimum difference between _any_ two nodes

Input / Output:


Notes:


Solution Approaches:
variation of tree iteration with tuple with node/min observed so far/max observed so far being sent
BST property of everything left is less than and everything right is greater than is crucial!

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = float('inf')
        queue = [(root, -1 * float('inf'), float('inf'))]
        while queue:
            curr_node, curr_min, curr_max = queue.pop(0)
            res = min(res, curr_node.val-curr_min, curr_max-curr_node.val)
            if curr_node.left:
                queue.append((curr_node.left, curr_min, curr_node.val))
            if curr_node.right:
                queue.append((curr_node.right, curr_node.val, curr_max))
        return res