"""
Link: https://leetcode.com/problems/invert-binary-tree/
Difficulty: easy

Problem:
invert a right and left nodes

Input / Output:


Notes:


Solution Approaches:
iteration over the tree. Use a temp node as a placeholder and swap left and right.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root:
            queue = [root]
            while queue:
                curr = queue.pop(0)
                temp = curr.right
                curr.right = curr.left
                curr.left = temp
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root