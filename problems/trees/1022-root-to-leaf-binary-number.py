"""
Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
Difficulty: easy

Problem:
Root-> Leaf forms binary number... sum and return all

Input / Output:


Notes:


Solution Approaches:
BFS for propigation and creation and convert/sum to res as you hit terminal condition

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = 0
        if not root: return res
        queue = [(root, [])]
        while queue:
            curr_node, binary = queue.pop(0)
            binary.append(curr_node.val)
            if not curr_node.right and not curr_node.left:
                for i,v in enumerate(binary[::-1]):
                    res += ((2**i)*v)
            if curr_node.right:
                queue.append((curr_node.right, binary[:]))
            if curr_node.left:
                queue.append((curr_node.left, binary[:]))
        return res