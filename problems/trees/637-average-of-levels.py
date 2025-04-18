"""
Link: https://leetcode.com/problems/average-of-levels-in-binary-tree
Difficulty: easy

Problem:
average value in each level of binary tree

Input / Output:


Notes:


Solution Approaches:
Breadth first to explore while using a list to sum and build next level

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root: return [0]
        res = []
        curr_level = [root]
        while curr_level:
            temp = []
            curr_sum = []
            for i in curr_level:
                curr_sum.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            sum = reduce(lambda x, y: x+y, curr_sum)
            res.append((sum*1.0)/len(curr_sum))
            curr_level = temp
        return res
