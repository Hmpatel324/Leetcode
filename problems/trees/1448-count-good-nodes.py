"""
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree
Difficulty: medium

Problem:
"Good" node: node in path from root such that no node in the path is greater
Return "good" nodes in tree

Input / Output:


Notes:


Solution Approaches:
Iteration through Tree via tuple
Tuple: (node, curr_max)
Seed: (root, -float(inf))

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root: return res
        queue = [(root, -float('inf'))]
        while queue:
            curr_node, curr_max = queue.pop(0)
            if curr_node.val >= curr_max: res+=1
            curr_max = max(curr_max, curr_node.val)
            if curr_node.left:
                queue.append((curr_node.left, curr_max))
            if curr_node.right:
                queue.append((curr_node.right, curr_max))
        return res
        