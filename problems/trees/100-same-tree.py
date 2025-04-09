"""
Link: https://leetcode.com/problems/same-tree
Difficulty: easy

Problem:
Are two trees the same value wise

Input / Output:


Notes:


Solution Approaches:
Iterative breadfirst solution to check p and q

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue = [(p,q)]
        while queue:
            curr_p, curr_q = queue.pop(0)
            if (curr_p and not curr_q) or (curr_q and not curr_p): return False
            curr_p_val = curr_p.val if curr_p else float('inf')
            curr_q_val = curr_q.val if curr_q else float('inf')
            if curr_p_val != curr_q_val: return False
            if(curr_p and curr_q):
                queue.append((curr_p.left, curr_q.left))
                queue.append((curr_p.right, curr_q.right))
        return True
