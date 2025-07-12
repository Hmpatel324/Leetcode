"""
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst
Difficulty: medium

Problem:
Find kth smallest value in a Binary search tree

Input / Output:


Notes:


Solution Approaches:
Key concept is that this is a bst - all left are smaller, all right are larger vs the "parent"
Effectively this problem become finding the kth item in a Depth First Search

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        counter = 0
        visited = set()
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr in visited:
                counter+=1
                if counter==k: return curr.val
            else:
                visited.add(curr)
                if curr.right: stack.append(curr.right)
                stack.append(curr)
                if curr.left: stack.append(curr.left)
        return -1