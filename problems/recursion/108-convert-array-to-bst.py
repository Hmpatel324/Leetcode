"""
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
Difficulty: easy

Problem:
Convert a ordered nums array into a bst

Input / Output:
int -> tree

Notes:
variation of binary search

Solution Approaches:
setup like binary search but unable to use iteration as you need to spawn threads to account for left and right

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, low, high, nums):
        res = TreeNode()
        if low == high:
            res.val = nums[low]
            print(res.val)
            return res
        elif low < high:
            mid = (low+high)/2
            res.val = nums[mid]
            res.left = self.helper(low, mid-1,nums)
            res.right = self.helper(mid+1,high, nums)
            return res
            
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        mid = (0+len(nums))/2
        res = TreeNode()
        res.val = nums[mid]
        res.left = self.helper(0, mid-1, nums)
        res.right = self.helper(mid+1, len(nums)-1, nums)
        return res
        
    
