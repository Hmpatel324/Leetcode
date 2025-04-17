"""
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Difficulty: easy

Problem:
Return post order traversal path of the tree

Input / Output:


Notes:


Solution Approaches:
DFS based stack iteration

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        if not root: return res
        visited = set()
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                stack.append(curr)
                if curr.right: stack.append(curr.right)
                if curr.left: stack.append(curr.left)
            else:
                res.append(curr.val)
        return res