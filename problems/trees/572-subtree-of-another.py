"""
Link: https://leetcode.com/problems/subtree-of-another-tree
Difficulty: easy

Problem:
Given main tree and a subtree, identify if the subtree exists in the main tree


Input / Output:


Notes:


Solution Approaches:
Breadth search for a initial root match then compare

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def helper(candidate_root):
            helper_queue = [(candidate_root, subRoot)]
            while helper_queue:
                curr_candidate_node, curr_sub_root_node = helper_queue.pop(0)
                if curr_candidate_node.val != curr_sub_root_node.val: return False
                if curr_sub_root_node.left:
                    if not curr_candidate_node.left: return False
                    helper_queue.append((curr_candidate_node.left, curr_sub_root_node.left))
                elif curr_candidate_node.left: return False
                if curr_sub_root_node.right:
                    if not curr_candidate_node.right: return False
                    helper_queue.append((curr_candidate_node.right, curr_sub_root_node.right))
                elif curr_candidate_node.right: return False
            return True

        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.val == subRoot.val:
                # check
                check = helper(curr)
                if check: return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False
