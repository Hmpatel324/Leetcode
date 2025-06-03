"""
Link: https://leetcode.com/problems/binary-tree-right-side-view/
Difficulty: medium

Problem:
List nodes if looking at a Tree from the right

Input / Output:


Notes:


Solution Approaches:
Level order traversal with output occuring at each level at index -1

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        if not root: return res
        queue = [root]
        while queue:
            curr = queue
            queue = None
            res.append(curr[-1].val)
            next_level = []
            for n in curr:
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
            if len(next_level) > 0: queue = next_level
        return res