"""
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
Difficulty: medium

Problem:
alternate level order result output

Input / Output:


Notes:


Solution Approaches:
iterative processing of each level. Use tuple to pass level nodes and is_left value fwd

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        queue = ([root], True)
        while queue:
            curr_level, is_left = queue
            queue = None
            next_level, temp = [], []
            for node_entry in curr_level:
                temp.append(node_entry.val)
                if node_entry.left:
                    next_level.append(node_entry.left)
                if node_entry.right:
                    next_level.append(node_entry.right)
            res.append(temp if is_left else temp[::-1])
            if next_level:
                queue = (next_level, not is_left)
        return res