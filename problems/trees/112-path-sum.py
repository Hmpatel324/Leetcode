"""
Link: https://leetcode.com/problems/path-sum
Difficulty: easy

Problem:
Return True if root to leaf sum equals target

Input / Output:


Notes:


Solution Approaches:
Breadth first search with tuple second slot being used to passdown sum

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        queue = [(root, 0)]
        while queue:
            curr_node, curr_val = queue.pop(0)
            curr_val += curr_node.val
            if not curr_node.right and not curr_node.left and targetSum == curr_val:
                return True
            if curr_node.right:
                queue.append((curr_node.right, curr_val))
            if curr_node.left:
                queue.append((curr_node.left, curr_val))
        return False