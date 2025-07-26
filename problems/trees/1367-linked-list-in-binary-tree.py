"""
Link: https://leetcode.com/problems/linked-list-in-binary-tree
Difficulty: medium

Problem:
Given a binary tree root and a linked list with head as the first node. 
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.


Input / Output:


Notes:


Solution Approaches:
Output LinkedList to List then use Breadth First tree exploration/track path.
If tail of a path == tail of linkedlist tail then perform a check. 

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        nums = []

        # Output Linked List into list
        while head:
            nums.append(head.val)
            head = head.next
        
        if not root or not nums: return False

        # Breadth First Exploration
        queue = [(root, [])]
        while queue:
            curr_node, curr_path = queue.pop(0)
            curr_path.append(curr_node.val)

            # Tail->Head comparison 
            if curr_path[-1] == nums[-1]:
                i = 1
                while i<=len(nums) and i<=len(curr_path):
                    if curr_path[-i] != nums[-i]:
                        break
                    i+=1
                if i>len(nums):return True # Terminal Condition
            
            # Append left and right
            if curr_node.left:
                queue.append((curr_node.left,curr_path[:]))
            if curr_node.right:
                queue.append((curr_node.right,curr_path[:]))
        return False