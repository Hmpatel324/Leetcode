"""
Link: https://leetcode.com/problems/balanced-binary-tree
Difficulty: easy

Problem:
Determine if left and right have a max height diff of 1

Input / Output:


Notes:


Solution Approaches:
Use cache to know right and left. Post-order DFS via stack / check. 

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root: return True
        stack = [root]
        visited = {}
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited[curr] = 0
                stack.append(curr)
                if curr.right: stack.append(curr.right)
                if curr.left: stack.append(curr.left)
            else:
                if not curr.left and not curr.right: visited[curr] = 0
                else:
                    right = (visited[curr.right]+1 if curr.right else 0)
                    left = (visited[curr.left]+1 if curr.left else 0)
                    if abs(left - right) > 1: return False
                    visited[curr] = max(left,right)
        return True