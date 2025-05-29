"""
Link: https://leetcode.com/problems/path-sum-ii
Difficulty: medium

Problem:
Find tree paths to root that have a sum of the targetsum

Input / Output:


Notes:


Solution Approaches:
BFS with queue with tuple (node, curr_path, curr_sum)
Check for leaf + sum else children check/add to queue

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        queue = [(root, [], 0)]
        while queue:
            curr_node, curr_path, curr_sum = queue.pop(0)
            curr_sum += curr_node.val
            curr_path.append(curr_node.val)
            if not curr_node.left and not curr_node.right and curr_sum==targetSum:
                res.append(curr_path)
            else:
                if curr_node.left:
                    queue.append((curr_node.left, [i for i in curr_path], curr_sum))
                if curr_node.right:
                    queue.append((curr_node.right, [i for i in curr_path], curr_sum))
        return res