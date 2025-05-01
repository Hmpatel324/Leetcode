"""
Link: https://leetcode.com/problems/binary-tree-tilt
Difficulty: easy

Problem:
find tilt and sum over tree
tilt is defined as abs(left sub- right sub)

Input / Output:


Notes:


Solution Approaches:
DFS and sum

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = 0
        if not root: return res
        visited = set()
        stack = [root]
        while stack:
            curr_og = stack.pop()
            if curr_og not in visited:
                visited.add(curr_og)
                stack.append(curr_og)
                if curr_og.right:
                    stack.append(curr_og.right)
                if curr_og.left:
                    stack.append(curr_og.left)
            else:
                left = 0 if not curr_og.left else curr_og.left.val
                right = 0 if not curr_og.right else curr_og.right.val
                res +=  abs(left-right)
                curr_og.val += (left+right)
        return res
