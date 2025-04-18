"""
Link: https://leetcode.com/problems/merge-two-binary-trees
Difficulty: easy

Problem:
Merge two binary trees together

Input / Output:


Notes:


Solution Approaches:
breadth first search to iterate then sum when both nodes present else move tree two into null tree 1 slots

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root1: return root2
        if not root2: return root1
        queue = [(root1, root2)]
        while queue:
            curr1, curr2 = queue.pop(0)
            curr1.val = curr1.val + curr2.val
            if curr1.left and curr2.left:
                queue.append((curr1.left, curr2.left))
            elif curr2.left:
                curr1.left = curr2.left
            if curr1.right and curr2.right:
                queue.append((curr1.right, curr2.right))
            elif curr2.right:
                curr1.right = curr2.right
        return root1